import torch.nn as nn

# self or cross attention
class Attention(nn.Module):
    def __init__(self, dim, n_heads=4, qkv_bias=True, attn_p=0., proj_p=0., cross=False):
        super().__init__()
        self.n_heads = n_heads
        self.dim = dim
        self.head_dim = dim // n_heads
        self.scale = self.head_dim ** -0.5
        
        self.qkv = nn.Linear(dim, dim * 3, bias=qkv_bias)
        self.cross = cross
        if cross:
            self.q_linear = nn.Linear(dim, dim, bias=qkv_bias)
            self.k_linear = nn.Linear(dim, dim, bias=qkv_bias)
            self.v_linear = nn.Linear(dim, dim, bias=qkv_bias)
        self.attn_drop = nn.Dropout(attn_p)
        self.proj = nn.Linear(dim, dim)
        self.proj_drop = nn.Dropout(proj_p)

    def forward(self, x):
        if self.cross:
            n_samples, n_tokens, dim = x[0].shape
            if dim != self.dim:
                raise ValueError

            n_tokens_en = n_tokens
            q = self.q_linear(x[0]).reshape(n_samples, n_tokens, self.n_heads, self.head_dim).permute(0, 2, 1, 3)
            k = self.k_linear(x[1]).reshape(n_samples, n_tokens_en, self.n_heads, self.head_dim).permute(0, 2, 1, 3)
            v = self.v_linear(x[2]).reshape(n_samples, n_tokens_en, self.n_heads, self.head_dim).permute(0, 2, 1, 3)
        else:
            n_samples, n_tokens, dim = x.shape
            if dim != self.dim:
                raise ValueError

            qkv = self.qkv(x)  # (n_samples, n_patches, 3 * dim)
            qkv = qkv.reshape(
                n_samples, n_tokens, 3, self.n_heads, self.head_dim
            )  # (n_smaples, n_patches, 3, n_heads, head_dim)
            qkv = qkv.permute(
                2, 0, 3, 1, 4
            )  # (3, n_samples, n_heads, n_patches, head_dim)
            q, k, v = qkv[0], qkv[1], qkv[2]

        k_t = k.transpose(-2, -1)  # (n_samples, n_heads, head_dim, n_patches + 1)
        dp = (q @ k_t) * self.scale  # (n_samples, n_heads, n_patches, n_patches)
        # exp(-x)
        # dp 过大，softmax之后数值可能溢出
        if self.cross:
            dp = -1 * dp
        attn = dp.softmax(dim=-1)  # (n_samples, n_heads, n_patches, n_patches)
        attn = self.attn_drop(attn)

        weighted_avg = attn @ v  # (n_samples, n_heads, n_patches +1, head_dim)
        weighted_avg = weighted_avg.transpose(1, 2)  # (n_samples, n_patches + 1, n_heads, head_dim)
        weighted_avg = weighted_avg.flatten(2)  # (n_samples, n_patches + 1, dim)

        x = self.proj(weighted_avg)  # (n_samples, n_patches + 1, dim)
        x = self.proj_drop(x)  # (n_samples, n_patches + 1, dim)
        
        return x