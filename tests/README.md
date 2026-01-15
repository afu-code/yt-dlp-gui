# 测试文件移动说明

## 变更内容

✅ **已移动**：`yt_dlp_gui/test_logic.py` → `tests/test_logic.py`

## 原因

- 更好的项目结构：所有测试文件集中在 `tests/` 目录
- 符合 Python 项目最佳实践
- 便于测试管理和执行

## 测试目录结构

```
tests/
├── __init__.py
├── test_basic.py      # 基础功能测试（配置、国际化、逻辑）
└── test_logic.py      # GUI 逻辑测试（unittest 格式）
```

## 运行测试

### 运行所有测试

```bash
# 使用 pytest（推荐）
pytest

# 使用 unittest
python -m unittest discover tests
```

### 运行特定测试文件

```bash
# pytest
pytest tests/test_logic.py -v
pytest tests/test_basic.py -v

# unittest
python -m unittest tests.test_logic -v
python -m unittest tests.test_basic -v
```

### 运行特定测试类或方法

```bash
# unittest
python -m unittest tests.test_logic.TestGUILogic -v
python -m unittest tests.test_logic.TestGUILogic.test_build_ydl_opts_basic -v
```

## 测试覆盖率

```bash
# 使用 pytest-cov
pytest --cov=yt_dlp_gui --cov-report=html

# 查看报告
# 打开 htmlcov/index.html
```

## 验证结果

✅ 所有测试通过：
```
test_build_ydl_opts_audio ... ok
test_build_ydl_opts_basic ... ok
test_executable_picker ... ok

Ran 3 tests in 0.114s
OK
```

## 注意事项

- `test_logic.py` 使用 `unittest` 框架
- `test_basic.py` 使用 `pytest` 框架
- 两种框架可以共存，pytest 可以运行 unittest 测试
- 建议统一使用 pytest 以获得更好的功能和报告
