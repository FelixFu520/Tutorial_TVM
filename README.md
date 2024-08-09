
## 官网教程
### [User Tutorial](https://github.com/apache/tvm/tree/main/gallery/tutorial)
`user_tutorial`文件夹中存放着官网的教程(`v0.18.dev0`)
```
1. TVM 原理简介
2. 安装 TVM
3. 使用命令行界面编译和优化模型
4. 使用 Python 接口编译和优化模型
5. 使用张量表达式操作算子
6. 使用模板和 AutoTVM 优化算子
7. 使用无模板的 AutoScheduler 优化算子
8. 交叉编译和远程过程调用（RPC）
9. 用 GPU 编译深度学习模型
```
1. Introduction(TVM原理介绍)——`user_tutorial/introduction.py`, [中文翻译](https://tvm.hyper.ai/docs/tutorial/intro)
2. Installing TVM(安装TVM)——`user_tutorial/install.py`, [中文翻译](https://tvm.hyper.ai/docs/tutorial/install)
3. Compiling and Optimizing a Model with TVMC(使用TVMC编译和优化模型)——`user_tutorial/tvmc_command_line_driver.py`, [中文翻译](https://tvm.hyper.ai/docs/tutorial/compile)
4. Getting Starting using TVMC Python: a high-level API for TVM(使用TVMC Python入门:TVM的高级API)——`user_tutorial/tvmc_python.py`, [中文翻译](https://tvm.hyper.ai/docs/tutorial/tvmc_python)
5. Compiling and Optimizing a Model with the Python Interface(使用Python接口(AutoTV)编译和优化模型)——`user_tutorial/autotvm_relay_x86.py`, [中文翻译](https://tvm.hyper.ai/docs/tutorial/python_AutoTVM)
6. Working with Operators using Tensor Expression(使用张量表达式处理算子)——`user_tutorial/tensor_expr_get_started.py`, [中文翻译](https://tvm.hyper.ai/docs/tutorial/tensor_expr)
7. Optimizing Operators with Schedule Templates and AutoTVM(用 Schedule 模板和 AutoTVM 优化算子)——`user_tutorial/autotvm_matmul_x86.py`, [中文翻译](https://tvm.hyper.ai/docs/tutorial/ops_AutoTVM)
8. Optimizing Operators witch Auto-scheduling(使用 Auto-scheduling 优化算子)——`user_tutorial/auto_scheduler_matmul_x86.py`, [中文翻译](https://tvm.hyper.ai/docs/tutorial/ops_AutoScheduling)
9. Blitz Course to TensorIR(TensorIR 快速入门)——`user_tutorial/tensor_ir_blitz_course.py`, [中文翻译](https://tvm.hyper.ai/docs/tutorial/tensorIR)
10. Cross Compilation and RPC(交叉编译和 RPC)——`user_tutorial/cross_compilation_and_rpc.py`, [中文翻译](https://tvm.hyper.ai/docs/tutorial/rpc)
11. Quick Start Tutorial for Compiling Deep Learning Models(快速入门：编译深度学习模型)——`user_tutorial/relay_quick_start.py`, [中文翻译](https://tvm.hyper.ai/docs/tutorial/quick_start)
12. Making your Hardware Accelerator TVM-ready with UMA(利用 UMA 使硬件加速器可直接用于 TVM)——`user_tutorial/uma.py`, [中文翻译](https://tvm.hyper.ai/docs/tutorial/uma)
13. Introduction to TOPI(TOPI简介)——`user_tutorial/intro_topi.py`, [中文翻译](https://tvm.hyper.ai/docs/tutorial/TOPI)

### [How To Guides](https://github.com/apache/tvm/tree/main/gallery/how_to)
1. Compile Deep Learning Models(编译深度学习模型), [EN](https://tvm.apache.org/docs/how_to/compile_models/index.html) | [CN](https://tvm.hyper.ai/docs/how_to/compile/)
2. Deploy Models and Integrate TVM(部署模型并与TVM集成), [EN](https://tvm.apache.org/docs/how_to/deploy/index.html) | [CN](https://tvm.hyper.ai/docs/how_to/deploy/)
3. Work with Relay(使用Relay), [EN](https://tvm.apache.org/docs/how_to/work_with_relay/index.html) | [CN](https://tvm.hyper.ai/docs/how_to/relay/)
4. Work with Tensor Expression and Schedules(使用张量表达式和 Schedule), [EN](https://tvm.apache.org/docs/how_to/work_with_schedules/index.html) | [CN](https://tvm.hyper.ai/docs/how_to/te_schedules/)
5. Optimize Tensor Operators(优化张量算子), [EN](https://tvm.apache.org/docs/how_to/optimize_operators/index.html) | [CN](https://tvm.hyper.ai/docs/how_to/optimize/)
6. Auto-Tune with Templates and AutoTVM(使用模板和 AutoTVM 进行自动调优), [EN](https://tvm.apache.org/docs/how_to/tune_with_autotvm/index.html) | [CN](https://tvm.hyper.ai/docs/how_to/autotune/)
7. Use AutoScheduler for Template-Free Scheduling(使用 AutoScheduler 进行无模板调度), [EN](https://tvm.apache.org/docs/how_to/tune_with_autoscheduler/index.html) | [CN](https://tvm.hyper.ai/docs/how_to/autoscheduler/)
8. Work with microTVM(使用 microTVM), [EN](https://tvm.apache.org/docs/how_to/work_with_microtvm/index.html) | [CN](https://tvm.hyper.ai/docs/how_to/microtvm/)
9. Extend TVM(扩展 TVM), [EN](https://tvm.apache.org/docs/how_to/extend_tvm/index.html) | [CN](https://tvm.hyper.ai/docs/how_to/extend/)
10. Profile Models(Profile 模型), [EN](https://tvm.apache.org/docs/how_to/profile/index.html) | [CN](https://tvm.hyper.ai/docs/how_to/models/)
11. Handle TVM Errors(处理 TVM 报错), [EN](https://tvm.apache.org/docs/errors.html) | [CN](https://tvm.hyper.ai/docs/how_to/errors)
12. Frequently Asked Questions(FAQ), [EN](https://tvm.apache.org/docs/faq.html) | [CN](https://tvm.hyper.ai/docs/how_to/FAQ)