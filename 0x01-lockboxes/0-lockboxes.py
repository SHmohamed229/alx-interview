#!/usr/bin/python3
"""this code be Solves the lock boxes puzzle """


def look_next_opened_box(opened_boxes):
    """this method for Looks for the next opened box
    Args:
         Opened_boxes (dict): dictionary which boxes already opened
    Returns:
        List: for List with  contained in the opened box
    """
    for index, box in opened_boxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('keys')
    return None


def canUnlockAll(boxes):
    """this method Check if all boxes can be opened
    Args:
        Boxes (list): for List  all the boxes with the keys
    Returns:
        Bool: for true if all boxes can be opened, otherwise,or  false
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    aux = {}
    while True:
        if len(aux) == 0:
            aux[0] = {
                'status': 'opened',
                'keys': boxes[0],
            }
        keys = look_next_opened_box(aux)
        if keys:
            for key in keys:
                try:
                    if aux.get(key) and aux.get(key).get('status') \
                       == 'opened/checked':
                        continue
                    aux[key] = {
                        'status': 'opened',
                        'keys': boxes[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in aux.values()]:
            continue
        elif len(aux) == len(boxes):
            break
        else:
            return False

    return len(aux) == len(boxes)


def main():
    """this method Entry point"""
    canUnlockAll([[]])


if __name__ == '__main__':
    main()
