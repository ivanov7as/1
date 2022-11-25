import export_data as exp
import import_data as imp
import view
import logger as log
def button_click():
    view.hello()
    choice = view.button()
    while choice !='q':
        log.log_info(choice)
        if choice == '1':
            exp.record_data()
        elif choice == '2':
            imp.find_element()
        choice=view.button()

