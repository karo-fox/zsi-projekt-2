import sys
from jinja2 import Template


def get_input_data(files_num):
    inputs = []
    for num in range(1, files_num + 1):
        with open(f"./in/in{num}.txt") as f:
            inputs.append(f.read())
    return inputs


def parse(files):
    data = []
    inputs = get_input_data(len(files))
    for idx, file in enumerate(files):
        with open(file) as f:
            content = f.readlines()
        data.append(
            {
                "idx": idx + 1,
                "input": inputs[idx],
                "result": content[-1],
                "counter": content[-2],
                "game": "".join(content[:-2]),
            }
        )
    return data


if __name__ == "__main__":
    try:
        files = sys.argv[1:]
    except ValueError:
        print("podano błędne dane wejściowe")

    template = Template(open("./template/index.html").read())
    data = parse(files)

    print(template.render(data=data))
