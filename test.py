"""
@name: hello
@description: 最简单的演示插件
"""
def main(*args, **kwargs):
    """插件主函数"""
    print("\nHello World from HSWTF Plugin!")
    
    # 保持规范返回结构
    return {"status": "success", "message": "printed hello world"}

# 测试代码
if __name__ == "__main__":
    main()