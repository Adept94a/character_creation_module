from random import randint


DEFAULT_ATTACK: int = 5
DEFAULT_DEFENCE: int = 10
DEFAULT_STAMINA: int = 80


class Character():
    BRIEF_DESC_CHAR_CLASS: str = 'отважный любитель приключений'
    RANGE_VALUE_ATTACK: tuple[int, int] = (1, 3)
    RANGE_VALUE_DEFENCE: tuple[int, int] = (1, 5)
    SPECIAL_SKILL: str = 'Удача'
    SPECIAL_BUFF: int = 15

    def __init__(self, name) -> None:
        self.name = name

    def attack(self):
        # Оператор * распаковывает передаваемый кортеж.
        value_attack: int = DEFAULT_ATTACK + randint(*self.RANG_CALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный {value_attack}')

    def defence(self):
        value_defence: int = DEFAULT_DEFENCE + randint(
                             *self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировад {value_defence} ед. урона')

    def special(self):
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".')

    def __str__(self):
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.'


class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS: str = (' дерзкий воин ближнего боя. '
                                  'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK: tuple[int, int] = (3, 5)
    RANGE_VALUE_DEFENCE: tuple[int, int] = (5, 10)
    SPECIAL_BUFF: int = DEFAULT_STAMINA + 25
    SPECIAL_SKILL: str = 'Выносливость'


class Mage(Character):
    BRIEF_DESC_CHAR_CLASS: str = (' находчивый воин дальнего боя. '
                                  'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK: tuple[int, int] = (5, 10)
    RANGE_VALUE_DEFENCE: tuple[int, int] = (-2, 2)
    SPECIAL_BUFF: int = DEFAULT_ATTACK + 40
    SPECIAL_SKILL: str = 'Атака'


class Healer(Character):
    BRIEF_DESC_CHAR_CLASS: str = (' могущественный заклинатель. '
                                  'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK: tuple[int, int] = (-3, -1)
    RANGE_VALUE_DEFENCE: tuple[int, int] = (2, 5)
    SPECIAL_BUFF: int = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL: str = 'Защита'


def choice_char_class(char_name: str) -> Character:
    """
    Возвращает строку с выбранным
    классом персонажа.
    """

    game_classes: tuple[str, str] = {'warrior': Warrior, 'mage': Mage,
                                     'healer': Healer}

    approve_choice: str = None

    while approve_choice != 'y':
        selected_class: str = input('Введи название персонажа, '
                                    'за которого хочешь играть: '
                                    'Воитель — warrior, '
                                    'Маг — mage, Лекарь — healer: ')
        char_class: Character = game_classes[selected_class](char_name)
        # Вывели в терминал описание персонажа.
        print(char_class)
        approve_choice: str = input('Нажми (Y), чтобы подтвердить выбор, '
                                    'или любую другую кнопку, '
                                    'чтобы выбрать другого персонажа ').lower()
    return char_class


def start_training(character: Character) -> None:
    """
    Принимает на вход имя и класс персонажа.
    Возвращает сообщения о результатах цикла тренировки персонажа.
    """
    commands: tuple[str, str] = {'attack': character.attack,
                                 'defence': character.defence,
                                 'special': character.special}
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd in commands:
            print(commands[cmd](character))
    return ('Тренировка окончена.')
