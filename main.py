import view
import model



def main():
    print("hello")
    map = model.world_map()
    view.print_start_screen()
    map.print_world()

if __name__ == "__main__":
    main()