from tvm.driver import tvmc

model = tvmc.load('res/resnet50-v2-7.onnx') # 第 1 步：加载
print(model.summary())

package = tvmc.compile(model, target='llvm') # 第 2 步：编译

result = tvmc.run(package, device='cpu') # 第 3 步：运行
print(result)

tvmc.tune(model, target='llvm', tuning_records='res/records.log') # 第 4 步：调优
