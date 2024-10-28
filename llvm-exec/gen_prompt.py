import os
from typing import List
from utils import create_file, remove_extra_blank_lines, remove_commented_lines

from pathlib import Path


def replace_single_braces(replacement, string, to_be_replaced="{}"):
    # replace the first occurrence of the to_be_replaced string
    return string.replace(f"{to_be_replaced}", replacement, 1)


def gen_prompt_from_template(
    func_list: list,
    func_body_list: list,
    example: str,
    passname: str,
    target_line: str,
    index: int,
    file_string: str,
    gen_dir_path: str = None,
    examples: List[str] = None,
) -> str:
    # if file_string == 'src2nl_gpt4':
    if "src2nl" in file_string:
        gen_src2nl_prompt_from_template(
            func_list,
            func_body_list,
            example,
            passname,
            target_line,
            index,
            file_string,
        )
        return

    if "starcoder_cpp_" in file_string:
        gen_prompt_nl2test(
            passname,
            index,
            file_string,
            gen_dir_path,
            examples,
        )
        return

    raise ValueError(f"file_string {file_string} not supported!")

#generate examples code
def examples_code(examples: List[str]):
    template = """# C++ Code begins

```cpp
{example}
```
# C++ Code ends
"""
    code = "\n".join([template.format(example=example) for example in examples])
    return code

#提示和例子都是一样的，只改了description（这是gpt生成的）
def gen_prompt_nl2test(
    passname: str,
    index: int,
    file_string: str,
    gen_dir_path: str,
    examples: List[str],
):
    """
    This function is used to generate the prompt for the feedback examples.
    """
    # Step 0: Check whether it is a feedback loop.
    is_feedback = False
    if "feedback" in file_string:
        is_feedback = True

    # Step 1: get the requirement description for the pass.
    NL_folder = f"source-code-data/llvm/llvm-gen-prompt/template_cpp_deadarg-new"
    model = "gpt-4"
    NL_path = os.path.join(
        NL_folder,
        passname + "oneshot" + f"_{index}" + f"_{model}_starcoder_cpp_deadarg.txt",
    )
    description = remove_commented_lines(NL_path, "...")

    # Step 2: get the template.
    with open(f"template_{file_string}.md", "r") as template:
        tpl = template.read()
    #replace the description
    tpl = replace_single_braces(description, tpl, "{Description}")
    # For the feedback loop, we need to fill in the examples.
    if is_feedback:
        tpl = replace_single_braces(examples_code(examples), tpl, "{Examples}")

    # Generate the prompt file.
    gen_dir_path = (
        gen_dir_path if gen_dir_path else "source-code-data/llvm/llvm-gen-prompt"
    )
    gen_dir = os.path.join(gen_dir_path)
    os.makedirs(gen_dir, exist_ok=True)
    gen_file_name = passname + "_oneshot" + f"_{index}.txt"
    gen_file = os.path.join(gen_dir, gen_file_name)
    create_file(gen_file)

    with open(gen_file, "w") as file:
        file.write(tpl)

    remove_extra_blank_lines(gen_file)
    print(f"prompt {gen_file} generated!")
    return


def generate_prompts(template_path, source_dir, output_dir):
    # 读取模板文件内容
    with open(template_path, 'r', encoding='utf-8') as template_file:
        template_content = template_file.read()
    
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 遍历源目录及其子目录
    for dirpath, dirnames, filenames in os.walk(source_dir):
        for filename in filenames:
            # 仅处理以 _1 结尾的 .txt 文件
            if filename.endswith('_1.txt'):
                file_path = os.path.join(dirpath, filename)
                
                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as source_file:
                    description_content = source_file.read()
                
                # 替换模板中的 {Description}
                prompt_content = template_content.replace('{Description}', description_content)

                # 生成新的文件名
                output_filename = filename.replace('_1.txt', 'startCoder.txt')
                output_file_path = os.path.join(output_dir, output_filename)
                
                # 写入新的文件
                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(prompt_content)
                
                print(f'生成文件: {output_file_path}')


def gen_src2nl_prompt_from_template(
    func_list: list,
    func_body_list: list,
    example: str,
    passname: str,
    target_line: str,
    index: int,
    file_string: str,
):
    with open(f"template_{file_string}.md", "r") as template:
        tpl = template.read()

    tpl = replace_single_braces(target_line, tpl, "{target_line}")
    tpl = replace_single_braces(func_list[0], tpl, "{first_fuction}")
    tpl = replace_single_braces(passname, tpl, "{Passname}")
    if "tutorial" not in file_string:
        tpl = replace_single_braces(passname, tpl, "{Passname}")
    tpl = replace_single_braces("\n\n".join(func_body_list), tpl, "{source_llvm}")

    gen_dir = os.path.join("source-code-data/llvm/llvm-gen-prompt", file_string)
    os.makedirs(gen_dir, exist_ok=True)
    gen_file = os.path.join(gen_dir, passname + "oneshot_" + f"{index}.txt")
    create_file(gen_file)

    with open(gen_file, "w") as file:
        file.write(tpl)

    remove_extra_blank_lines(gen_file)
    print(f"{file_string} prompt {gen_file} generated!")
    pass


"""
Generate prompt test.
"""


def test_prompt_feedback():
    passname = "ADCEPass"
    index = 0
    file_string = "starcoder_cpp_feedback"
    gen_prompt_nl2test(
        passname,
        index,
        file_string,
        gen_dir_path="test",
        examples=["int main() { return 0; }", "int main() { return 1; }"],
    )


def test_prompt_nl2test():
    passname = "ADCEPass"
    index = 0
    file_string = "starcoder_cpp_deadarg"
    gen_prompt_nl2test(
        passname,
        index,
        file_string,
        gen_dir_path="test",
        examples=["int main() { return 0; }", "int main() { return 1; }"],
    )


if __name__ == "__main__":
    #test_prompt_feedback()
    # test_prompt_nl2test()
    template_path = 'starcoder-mixnl2test-oneshot.md'  # 模板文件路径
    source_dir = 'source-code-data/llvm/llvm-gen-prompt/llvm/req'  # 源文件夹路径
    output_dir = 'Prompt-llvm-startCoder'  # 输出文件夹路径
    generate_prompts(template_path, source_dir, output_dir)
