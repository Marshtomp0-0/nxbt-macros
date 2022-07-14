import sys
import time

import nxbt
from nxbt import Buttons

MACRO = """
A 0.1S
0.5S
A 0.1S
6S
L_STICK@+100-000 0.1S
0.25S
PLUS 0.1S
0.5S
ZR 0.1S
0.25S
DPAD_DOWN 0.1S
0.25S
A 0.1S
0.5S
R 0.1S
0.25S
R 0.1S
0.25S
A 0.1S
1S
R 0.1S
0.5S
R 0.1S
1S
ZR 0.1S
0.5S
DPAD_DOWN 0.1S
0.25S
A 0.1S
0.25S
X 0.1S
0.25S
DPAD_UP 0.1S
0.25S
A 0.1S
0.25S
3S
L_STICK@+000+100 5S
R_STICK@-100+000 0.2S
L_STICK@+000+100 1S
LOOP 280
    R X 0.1S
    R Y 0.1S
    0.25S
LOOP 30
    PLUS 0.1S
    0.25S
R 0.1S
1S
DPAD_UP 0.1S
0.5S
DPAD_UP 0.1S
0.5S
A 0.1S
3S
DPAD_DOWN 0.1S
0.5S
DPAD_DOWN 0.1S
0.5S
DPAD_DOWN 0.1S
0.5S
DPAD_DOWN 0.1S
1S
A 0.1S
3S
A 0.1S
10S
A 0.1S
2S
A 0.1S
2S
B 0.1S
2S
DPAD_UP 0.1S
0.25S
DPAD_UP 0.1S
0.25S
5S
"""

M1_ENTER_BATTLE="""
A 0.1S
0.5S
A 0.1S
6S
"""

M2_SET_ADJUNCT="""
L_STICK@+100-000 0.1S
0.25S
PLUS 0.1S
0.5S
ZR 0.1S
0.25S
DPAD_DOWN 0.1S
0.25S
A 0.1S
0.5S
R 0.1S
0.25S
R 0.1S
0.25S
A 0.1S
1S
R 0.1S
0.5S
R 0.1S
1S
ZR 0.1S
0.5S
DPAD_DOWN 0.1S
0.25S
A 0.1S
0.25S
"""

M3_MOVE_TO_GATE="""
X 0.1S
0.25S
DPAD_UP 0.1S
0.25S
A 0.1S
0.25S
3S
L_STICK@+000+100 5S
R_STICK@-100+000 0.2S
L_STICK@+000+100 1S
"""

M4_SPAM_RX_RY="""
LOOP 280
    R X 0.1S
    R Y 0.1S
    0.25S
"""

M5_COMFIRM_BATTLE_RESULT="""
LOOP 30
    PLUS 0.1S
    0.25S
"""

M6_NAVIGATE_BACK_TO_BATTLE="""
R 0.1S
1S
DPAD_UP 0.1S
0.5S
DPAD_UP 0.1S
0.5S
A 0.1S
3S
DPAD_DOWN 0.1S
0.5S
DPAD_DOWN 0.1S
0.5S
DPAD_DOWN 0.1S
0.5S
DPAD_DOWN 0.1S
1S
A 0.1S
3S
A 0.1S
10S
A 0.1S
2S
A 0.1S
2S
B 0.1S
2S
DPAD_UP 0.1S
0.25S
DPAD_UP 0.1S
0.25S
5S
"""

if __name__ == "__main__":
    try:
        print("init nxbt")
        # Init NXBT
        nx = nxbt.Nxbt()

        # Get a list of all previously connected Switches and pass it as a reconnect_address argument
        controller_index = nx.create_controller(
            nxbt.PRO_CONTROLLER,
            reconnect_address=nx.get_switch_addresses())

        print("start waiting ", nx.get_switch_addresses())
        nx.wait_for_connection(controller_index)
        time.sleep(10)
        nx.press_buttons(controller_index, [Buttons.A])
        time.sleep(2)
        print("Connected")

        i = 0
        while True:
            print(f"Running Macro: Iteration {i}")
            # macro_id = nx.macro(controller_index, MACRO)
            print("enter battle")
            macro_id = nx.macro(controller_index, M1_ENTER_BATTLE)
            print("set adjunct")
            macro_id = nx.macro(controller_index, M2_SET_ADJUNCT)
            print("move to gate")
            macro_id = nx.macro(controller_index, M3_MOVE_TO_GATE)
            print("spam rx ry")
            macro_id = nx.macro(controller_index, M4_SPAM_RX_RY)
            print("confirm battle result")
            macro_id = nx.macro(controller_index, M5_COMFIRM_BATTLE_RESULT)
            print("navigate back to battle")
            macro_id = nx.macro(controller_index, M6_NAVIGATE_BACK_TO_BATTLE)
            i = i + 1
    except KeyboardInterrupt:
        print("Exiting...")
        nx.clear_all_macros()
        nx.remove_controller(controller_index)
        print("Bye")
    sys.exit(0)
        