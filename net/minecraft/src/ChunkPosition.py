# // Decompiled by Jad v1.5.8g. Copyright 2001 Pavel Kouznetsov.
# // Jad home page: http://www.kpdus.com/jad.html
# // Decompiler options: packimports(3) braces deadcode fieldsfirst 
# 
# package net.minecraft.src;
# 
# 
# // Referenced classes of package net.minecraft.src:
# //            Vec3D, MathHelper
# 
# public class ChunkPosition
# {
# 
#     public final int x;
#     public final int y;
#     public final int z;
# 
#     public ChunkPosition(int i, int j, int k)
#     {
#         x = i;
#         y = j;
#         z = k;
#     }
# 
#     public ChunkPosition(Vec3D vec3d)
#     {
#         this(MathHelper.floor_double(vec3d.xCoord), MathHelper.floor_double(vec3d.yCoord), MathHelper.floor_double(vec3d.zCoord));
#     }
# 
#     public boolean equals(Object obj)
#     {
#         if(obj instanceof ChunkPosition)
#         {
#             ChunkPosition chunkposition = (ChunkPosition)obj;
#             return chunkposition.x == x && chunkposition.y == y && chunkposition.z == z;
#         } else
#         {
#             return false;
#         }
#     }
# 
#     public int hashCode()
#     {
#         return x * 0x88f9fa + y * 0xef88b + z;
#     }
# }
