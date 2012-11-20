import commands

def play(sound_path, times):
    play_file = 'mpg123 -q ' + sound_path
    for i in range(times):
    	commands.getoutput(play_file)
    	if i == 5: break
    

