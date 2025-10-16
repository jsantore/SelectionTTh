import dearpygui.dearpygui as gui
import comp151Colors
BAR_HEIGHT = 100
next_bar_start = 50
bar_color = comp151Colors.GRAY
data_file = open("MovievsGames.txt", 'r')
data = data_file.readlines()
gui.create_context()
gui.create_viewport(title="Movie vs. Games", width=1000, height=1000)
with gui.window(label="Movie vs. Games", width=1000, height=1000):
    with gui.drawlist(width=1000, height=1000) as draw_list:
        for line in data:
            line_data = line.split(":")
            game_money = float(line_data[2])
            movie_money = float(line_data[1])
            bar_width = game_money*10
            if movie_money > game_money:
                bar_color = comp151Colors.DARK_PURPLE
            else:
                bar_color = comp151Colors.RED
            gui.draw_rectangle((0,next_bar_start), (bar_width, next_bar_start+BAR_HEIGHT),
                               fill=bar_color)
            next_bar_start += BAR_HEIGHT+30



gui.setup_dearpygui()
gui.show_viewport()
gui.start_dearpygui()
gui.destroy_context()