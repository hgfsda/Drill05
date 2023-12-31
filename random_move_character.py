from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 800, 600
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

hand_x, hand_y, hand_check, dir_check = 0,0, False,0
def create_hand():
    global x, hand_x, hand_y, hand_check, dir_check
    hand_x, hand_y, hand_check = random.randint(100, 700), random.randint(100, 600), True
    if x > hand_x:
        dir_check = 0
    else:
        dir_check = 1

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
save_x, save_y = x, y
i, frame = 0, 0
hide_cursor()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if hand_check == False:
        create_hand()

    if dir_check == 0:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
    elif dir_check == 1:
        character.clip_draw(frame * 100, 100, 100, 100, x, y)

    t = i / 500
    x = (1 - t) * save_x + t * hand_x
    y = (1 - t) * save_y + t * hand_y
    i = i + 1
    if i == 500:
        i = 0
        save_x, save_y = x, y
        hand_check = False

    hand.draw(hand_x, hand_y)
    update_canvas()
    frame = (frame + 1) % 8
    handle_events()

close_canvas()




