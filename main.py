import readchar

def print_menu(options, selected_index):
    for i, option in enumerate(options):
        if i == selected_index:
            print(f"> * {option}")
        else:
            print(f"    {option}")

def menu():
    options = ["Opção 1", "Opção 2", "Opção 3"]
    selected_index = 0

    while True:
        print("\n" * 100)  # Limpa a tela no console
        print_menu(options, selected_index)

        key = readchar.readkey()

        if key == readchar.key.UP and selected_index > 0:
            selected_index -= 1
        elif key == readchar.key.DOWN and selected_index < len(options) - 1:
            selected_index += 1
        elif key in [readchar.key.ENTER, "\r", "\n"]:
            print(f"Opção selecionada: {options[selected_index]}")
            break


if __name__ == "__main__":
    menu()
