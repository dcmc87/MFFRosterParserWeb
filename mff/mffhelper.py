import datetime

import Levenshtein
import jsonpickle
from PIL import Image
from mff.databasehelper import *
from mff.ocr import Ocr
import math


ASPECT_RATIO_16_9 = 1.777777
ASPECT_RATIO_16_10 = 1.6
ASPECT_RATIO_4_3 = 1.3333333
ASPECT_RATIO_185_9 = 2.055555
ASPECT_RATIO_15_10 = 1.5


class UnsupportedRatioException(ValueError):
    pass


ocr_ob = Ocr()


class Rects:
    def __init__(self, width: int, height: int):

        aspect = width / height
        scale = 1.


        def scale_rect(rect):
            return tuple(int(scale * i) for i in rect)

        if math.isclose(ASPECT_RATIO_16_9, aspect, rel_tol=0.04):
            scale = width / 1920
            print(scale)

            self.rect_check_details_page = scale_rect((586, 184, 733, 223))
            self.rect_check_gear_page = scale_rect((156, 23, 313, 74))
            self.rect_gear_name = scale_rect((387, 143, 1018, 187))

            self.rect_tier = scale_rect((460, 393, 555, 427))
            self.rect_char = scale_rect((104, 479, 546, 520))
            self.rect_uni = scale_rect((108, 523, 554, 560))
            self.rect_phys_att = scale_rect((911, 240, 1186, 280))
            self.rect_energy_att = scale_rect((911, 280, 1186, 327))
            self.rect_atk_spd = scale_rect((911, 327, 1186, 374))
            self.rect_crit_rate = scale_rect((911, 374, 1186, 423))
            self.rect_crit_dam = scale_rect((911, 423, 1186, 468))
            self.rect_def_pen = scale_rect((911, 468, 1186, 517))
            self.rect_ignore_dodge = scale_rect((911, 517, 1186, 568))
            self.rect_phys_def = scale_rect((1530, 238, 1816, 280))
            self.rect_energy_def = scale_rect((1530, 280, 1816, 329))
            self.rect_hp = scale_rect((1530, 329, 1816, 376))
            self.rect_recorate = scale_rect((1530, 376, 1816, 421))
            self.rect_dodge = scale_rect((1530, 421, 1816, 472))
            self.rect_mv_spd = scale_rect((1541, 810, 1814, 847))
            self.rect_debuff = scale_rect((1653, 856, 1816, 895))
            self.rect_scd = scale_rect((1666, 903, 1816, 937))

            self.list_rect_gearstat = list()
            self.list_rect_gearstat.append(scale_rect((400, 304, 1024, 349)))
            self.list_rect_gearstat.append(scale_rect((400, 348, 1024, 384)))
            self.list_rect_gearstat.append(scale_rect((400, 390, 1024, 432)))
            self.list_rect_gearstat.append(scale_rect((400, 434, 1024, 475)))
            self.list_rect_gearstat.append(scale_rect((400, 477, 1024, 517)))
            self.list_rect_gearstat.append(scale_rect((400, 521, 1024, 559)))
            self.list_rect_gearstat.append(scale_rect((400, 564, 1024, 603)))
            self.list_rect_gearstat.append(scale_rect((400, 606, 1024, 646)))

        elif math.isclose(ASPECT_RATIO_16_10, aspect, rel_tol=0.04):
            scale = width / 1600
            print(scale)

            self.rect_check_details_page = scale_rect((469, 183, 588, 215))
            self.rect_check_gear_page = scale_rect((143, 15, 274, 67))
            self.rect_gear_name = scale_rect((285, 147, 859, 186))

            self.rect_tier = scale_rect((352, 367, 442, 400))
            self.rect_char = scale_rect((41, 446, 441, 482))
            self.rect_uni = scale_rect((41, 482, 441, 520))
            self.rect_phys_att = scale_rect((470, 230, 1000, 268))
            self.rect_energy_att = scale_rect((470, 268, 1000, 313))
            self.rect_atk_spd = scale_rect((470, 313, 1000, 354))
            self.rect_crit_rate = scale_rect((470, 354, 1000, 396))
            self.rect_crit_dam = scale_rect((470, 396, 1000, 437))
            self.rect_def_pen = scale_rect((470, 437, 1000, 482))
            self.rect_ignore_dodge = scale_rect((470, 482, 1000, 522))
            self.rect_phys_def = scale_rect((1028, 231, 1560, 271))
            self.rect_energy_def = scale_rect((1028, 271, 1560, 313))
            self.rect_hp = scale_rect((1028, 313, 1560, 354))
            self.rect_recorate = scale_rect((1028, 354, 1560, 397))
            self.rect_dodge = scale_rect((1028, 397, 1560, 439))
            self.rect_mv_spd = scale_rect((1028, 738, 1560, 778))
            self.rect_debuff = scale_rect((1028, 778, 1560, 817))
            self.rect_scd = scale_rect((1028, 817, 1560, 860))

            self.list_rect_gearstat = list()
            self.list_rect_gearstat.append(scale_rect((300, 290, 859, 325)))
            self.list_rect_gearstat.append(scale_rect((300, 325, 859, 365)))
            self.list_rect_gearstat.append(scale_rect((300, 365, 859, 405)))
            self.list_rect_gearstat.append(scale_rect((300, 405, 859, 443)))
            self.list_rect_gearstat.append(scale_rect((300, 443, 859, 479)))
            self.list_rect_gearstat.append(scale_rect((300, 479, 859, 518)))
            self.list_rect_gearstat.append(scale_rect((300, 518, 859, 556)))
            self.list_rect_gearstat.append(scale_rect((300, 556, 859, 596)))

        elif math.isclose(ASPECT_RATIO_4_3, aspect, rel_tol=0.04):
            scale = width / 1778
            print(scale)

            self.rect_check_details_page = scale_rect((520, 316, 655, 355))
            self.rect_check_gear_page = scale_rect((158, 16, 298, 77))
            self.rect_gear_name = scale_rect((325, 273, 960, 320))

            self.rect_tier = scale_rect((395, 515, 490, 555))
            self.rect_char = scale_rect((43, 604, 489, 647))
            self.rect_uni = scale_rect((43, 647, 490, 683))
            self.rect_phys_att = scale_rect((520, 368, 1113, 411))
            self.rect_energy_att = scale_rect((520, 411, 1113, 459))
            self.rect_atk_spd = scale_rect((520, 459, 1113, 506))
            self.rect_crit_rate = scale_rect((520, 506, 1113, 553))
            self.rect_crit_dam = scale_rect((520, 553, 1113, 597))
            self.rect_def_pen = scale_rect((520, 597, 1113, 645))
            self.rect_ignore_dodge = scale_rect((520, 645, 1113, 691))
            self.rect_phys_def = scale_rect((1143, 369, 1736, 412))
            self.rect_energy_def = scale_rect((1143, 412, 1736, 458))
            self.rect_hp = scale_rect((1143, 458, 1736, 504))
            self.rect_recorate = scale_rect((1143, 504, 1736, 552))
            self.rect_dodge = scale_rect((1143, 552, 1736, 602))
            self.rect_mv_spd = scale_rect((1143, 931, 1736, 977))
            self.rect_debuff = scale_rect((1143, 977, 1736, 1022))
            self.rect_scd = scale_rect((1143, 1022, 1736, 1066))

            self.list_rect_gearstat = list()
            self.list_rect_gearstat.append(scale_rect((337, 434, 959, 474)))
            self.list_rect_gearstat.append(scale_rect((337, 474, 959, 518)))
            self.list_rect_gearstat.append(scale_rect((337, 518, 959, 560)))
            self.list_rect_gearstat.append(scale_rect((337, 560, 959, 602)))
            self.list_rect_gearstat.append(scale_rect((337, 602, 959, 646)))
            self.list_rect_gearstat.append(scale_rect((337, 646, 959, 686)))
            self.list_rect_gearstat.append(scale_rect((337, 686, 959, 730)))
            self.list_rect_gearstat.append(scale_rect((337, 730, 959, 772)))

        elif math.isclose(ASPECT_RATIO_185_9, aspect, rel_tol=0.04):
            scale = width / 1776
            print(scale)

            self.rect_check_details_page = scale_rect((590, 146, 698, 176))
            self.rect_check_gear_page = scale_rect((127, 17, 248, 58))
            self.rect_gear_name = scale_rect((427, 114, 948, 155))

            self.rect_tier = scale_rect((487, 314, 564, 343))
            self.rect_char = scale_rect((202, 384, 564, 416))
            self.rect_uni = scale_rect((202, 416, 564, 447))
            self.rect_phys_att = scale_rect((590, 190, 1069, 224))
            self.rect_energy_att = scale_rect((590, 224, 1069, 263))
            self.rect_atk_spd = scale_rect((590, 263, 1069, 301))
            self.rect_crit_rate = scale_rect((590, 301, 1069, 341))
            self.rect_crit_dam = scale_rect((590, 341, 1069, 377))
            self.rect_def_pen = scale_rect((590, 377, 1069, 413))
            self.rect_ignore_dodge = scale_rect((590, 413, 1069, 451))
            self.rect_phys_def = scale_rect((1093, 188, 1572, 225))
            self.rect_energy_def = scale_rect((1093, 225, 1572, 265))
            self.rect_hp = scale_rect((1093, 265, 1572, 301))
            self.rect_recorate = scale_rect((1093, 301, 1572, 339))
            self.rect_dodge = scale_rect((1093, 339, 1572, 377))
            self.rect_mv_spd = scale_rect((1093, 646, 1572, 682))
            self.rect_debuff = scale_rect((1093, 682, 1572, 720))
            self.rect_scd = scale_rect((1093, 720, 1572, 756))

            self.list_rect_gearstat = list()
            self.list_rect_gearstat.append(scale_rect((439, 243, 942, 277)))
            self.list_rect_gearstat.append(scale_rect((439, 277, 942, 310)))
            self.list_rect_gearstat.append(scale_rect((439, 310, 942, 346)))
            self.list_rect_gearstat.append(scale_rect((439, 346, 942, 379)))
            self.list_rect_gearstat.append(scale_rect((439, 379, 942, 414)))
            self.list_rect_gearstat.append(scale_rect((439, 414, 942, 447)))
            self.list_rect_gearstat.append(scale_rect((439, 447, 942, 482)))
            self.list_rect_gearstat.append(scale_rect((439, 482, 942, 520)))

        else:
            raise UnsupportedRatioException


list_gear_val = ("physical_attack_by_level",
                 "physical_attack",
                 "energy_attack_by_level",
                 "energy_attack",
                 "hp_by_level",
                 "hp",
                 "defense_penetration",
                 "critical_rate",
                 "critical_damage",
                 "skill_cooldown",
                 "attack_speed",
                 "all_attack",
                 "dodge",
                 "movement_speed",
                 "recovery_rate",
                 "physical_defense_by_level",
                 "energy_defense_by_level",
                 "physical_defense",
                 "energy_defense",
                 "all_defense")
list_gear_statname = ("physicalattackperlv.",
                      "physicalattack",
                      "energyattackperlv.",
                      "energyattack",
                      "hpperlv.",
                      "hp",
                      "ignoredefense",
                      "criticalrate",
                      "criticaldamage",
                      "skillcooldown",
                      "attackspeed",
                      "allattacks",
                      "dodge",
                      "movementspeed",
                      "recoveryrate",
                      "physicaldefenseperlv.",
                      "energydefenseperlv.",
                      "physicaldefense",
                      "energydefense",
                      "alldefenses")



class GearValue:
    def __init__(self):
        self.type = ""
        self.val = 0.
        self.pref = False


class Attack:
    def __init__(self):
        self.physical = 0
        self.energy = 0


class Defense:
    def __init__(self):
        self.physical = 0
        self.energy = 0


class Character:
    def __init__(self, char_alias=""):
        self.id = char_alias
        self.uniform = ""
        self.uniforms = {}
        self.tier = 1
        self.attack = Attack()
        self.defense = Defense()
        self.hp = 0
        self.dodge = 0.
        self.ignore_dodge = 0.
        self.defpen = 0.
        self.scd = 0.
        self.critrate = 0.
        self.critdamage = 0.
        self.atkspeed = 0.
        self.recorate = 0.
        self.movspeed = 0.
        self.debuff = 0.
        self.skills = [1, 1, 1, 1, 1]
        self.gear = [[GearValue() for i in range(8)] for j in range(4)]
        self.lastUpdate = 0


    # remove last 2 attributes from state so jsonpickler does not serialise them
    def __getstate__(self):
        state = self.__dict__.copy()
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)


def greyscale_ocr(image, rect, threshold=140):
    return ocr_ob.ocr_using_greyscale(image.crop(rect), threshold)

def color_ocr_text(image, rect, color=(255, 255, 255), threshold=20, inverted_colors=False, erode=False):
    return ocr_ob.ocr_using_color_similarity(image.crop(rect), color, threshold,  inverted_colors, erode)

def color_ocr_int(image, rect, color=(255,255,255), threshold=20, inverted_colors=False, erode=False):
    num = ocr_ob.ocr_using_color_similarity(image.crop(rect), color, threshold,  inverted_colors, erode)
    try:
        num = int(num)
    except:
        num = 0
    return num

def color_ocr_float(image, rect, color=(255,255,255), threshold=20, inverted_colors=False, erode=False):
    num = ocr_ob.ocr_using_color_similarity(image.crop(rect), color, threshold, inverted_colors, erode)
    try:
        num = float(num)
    except:
        num = 0.
    return num


def get_gear(screenshot, rects):

    # split gear state rectangle into left and right
    def split_gear_rect(rect):
        return ((rect[0], rect[1], int((rect[2] - rect[0]) * 0.7 + rect[0]), rect[3]),
                (rect[2] - int((rect[2] - rect[0]) * 0.3), rect[1], rect[2], rect[3]))

    def do_ocr(image, rect):
        stat_rects = split_gear_rect(rect)
        left_rect = stat_rects[0]
        right_rect = stat_rects[1]

        type = ""
        raw_type = greyscale_ocr(image, left_rect,  threshold=110).replace(" ", "").lower()
        if raw_type != "":
            for i, item in enumerate(list_gear_statname):
                if item in raw_type:
                    type = list_gear_val[i]
                    break
            if type == "":
                for i, item in enumerate(list_gear_statname):
                    if Levenshtein.distance(item, raw_type) < 3:
                        type = list_gear_val[i]
                        break

        val = color_ocr_text(image, right_rect, color=(10, 18, 35), threshold=80, inverted_colors=True, erode=True).replace(" ", "").replace("%", "").replace("+", "").replace('"', "4").replace("s", "5")
        # val = greyscale_ocr(image, right_rect, threshold=145).replace(" ", "").replace("%", "").replace("+", "").replace('"', "4")
        if val != "":
            try:
                val = float(val)
            except:
                val = 0.
        else:
            val = 0.

        return type, val

    gear = [GearValue() for i in range(8)]
    for i, item in enumerate(rects):
        gear[i].type, gear[i].val = do_ocr(screenshot, rects[i])
    return gear


def get_char_json(filepath):

    screenshot = Image.open(filepath)

    now = datetime.datetime.now()
    desiredwidth = 1920
    scale = desiredwidth / screenshot.size[0]
    if screenshot.size[0]< desiredwidth:
        screenshot= screenshot.resize((desiredwidth, int(scale*screenshot.size[1])), Image.NEAREST)
    elif screenshot.size[0]>desiredwidth:
        screenshot.thumbnail((int(screenshot.size[0]*scale), int(screenshot.size[1]*scale)))
    print("scaled in "+str(datetime.datetime.now()-now))

    time = datetime.datetime.now()
    width = screenshot.size[0]
    height = screenshot.size[1]
    # define rects based on aspect ratio

    try:
        rects = Rects(width, height)
    except UnsupportedRatioException:
        return None

    if greyscale_ocr(screenshot, rects.rect_check_details_page, threshold=120).replace(" ", "") == "attack":

        char = Character()

        char.tier = 2 if ("2" in color_ocr_text(screenshot, rects.rect_tier, (8, 20, 34), threshold=80, inverted_colors=True, erode=True, ).replace("z", "2")) else 1
        char.id = get_char_alias(greyscale_ocr(screenshot, rects.rect_char, 220))
        char.uniform = get_uniform_alias(greyscale_ocr(screenshot, rects.rect_uni, 180))

        t = 40
        erode = True

        char.attack.physical = color_ocr_int(screenshot, rects.rect_phys_att, (255, 255, 255), threshold=t, erode=erode)
        char.attack.energy = color_ocr_int(screenshot, rects.rect_energy_att, (255, 255, 255), threshold = t, erode = erode)
        char.atkspeed = color_ocr_float(screenshot, rects.rect_atk_spd, (255, 255, 255), threshold=t, erode = erode)
        char.critrate = color_ocr_float(screenshot, rects.rect_crit_rate, (255, 255, 255), threshold=t, erode = erode)
        char.critdamage = color_ocr_float(screenshot, rects.rect_crit_dam, (255, 255, 255), threshold=t, erode = erode)
        char.defpen = color_ocr_float(screenshot, rects.rect_def_pen, (255, 255, 255), threshold=t, erode = erode)
        char.ignore_dodge = color_ocr_float(screenshot, rects.rect_ignore_dodge, (255, 255, 255), threshold=t, erode = erode)
        char.defense.physical = color_ocr_int(screenshot, rects.rect_phys_def, (255, 255, 255), threshold=t, erode = erode)
        char.defense.energy = color_ocr_int(screenshot, rects.rect_energy_def, (255, 255, 255), threshold=t, erode = erode)
        char.hp = color_ocr_int(screenshot, rects.rect_hp, (255, 255, 255), threshold=t, erode = erode)
        char.recorate = color_ocr_float(screenshot, rects.rect_recorate, (255, 255, 255), threshold=t, erode = erode)
        char.dodge = color_ocr_float(screenshot, rects.rect_dodge, (255, 255, 255), threshold=t, erode = erode)
        char.movspeed = color_ocr_float(screenshot, rects.rect_mv_spd, (255, 255, 255), threshold=t, erode = erode)
        char.debuff = color_ocr_float(screenshot, rects.rect_debuff, (255, 255, 255), threshold=t, erode = erode)
        char.scd = color_ocr_float(screenshot, rects.rect_scd, (255, 255, 255), threshold=t, erode = erode)

        # char.tier = 2 if ("2" in greyscale_ocr(screenshot, rects.rect_tier, 180)) else 1
        # char.id = get_char_alias(greyscale_ocr(screenshot, rects.rect_char, 180))
        # char.uniform = get_uniform_alias(greyscale_ocr(screenshot, rects.rect_uni, 180))
        # char.attack.physical = greyscale_ocr(screenshot, rects.rect_phys_att, 160)
        # char.attack.energy = greyscale_ocr(screenshot, rects.rect_energy_att, 180)
        # char.atkspeed = greyscale_ocr(screenshot, rects.rect_atk_spd, 180)
        # char.critrate = greyscale_ocr(screenshot, rects.rect_crit_rate, 180)
        # char.critdamage = greyscale_ocr(screenshot, rects.rect_crit_dam, 180)
        # char.defpen = greyscale_ocr(screenshot, rects.rect_def_pen, 180)
        # char.ignore_dodge = greyscale_ocr(screenshot, rects.rect_ignore_dodge, 180)
        # char.defense.physical = greyscale_ocr(screenshot, rects.rect_phys_def, 180)
        # char.defense.energy = greyscale_ocr(screenshot, rects.rect_energy_def, 180)
        # char.hp = greyscale_ocr(screenshot, rects.rect_hp, 180)
        # char.recorate = greyscale_ocr(screenshot, rects.rect_recorate, 180)
        # char.dodge = greyscale_ocr(screenshot, rects.rect_dodge, 180)
        # char.movspeed = greyscale_ocr(screenshot, rects.rect_mv_spd, 180)
        # char.debuff = greyscale_ocr(screenshot, rects.rect_debuff, 180)
        # char.scd = greyscale_ocr(screenshot, rects.rect_scd, 180)

        return {"result_char": char, "filepath": filepath, "gear_num":-1, "gear_name":None}

    elif greyscale_ocr(screenshot, rects.rect_check_gear_page, threshold=140).replace(" ", "") == "gear":

        gear_name = color_ocr_text(screenshot, rects.rect_gear_name, threshold=40, color=(255, 255, 255))
        # returns list of dicts from DB with format (char_alias, gear_name, gear_num)
        char_list = get_chars_from_gear(gear_name)

        # if managed to match to exactly 1 character, return character json, else :
        char = Character()
        gear_num = -1

        if len(char_list)==0:
           return filepath
        if len(char_list) == 1:
            char.id = char_list[0]["char_alias"]
            # database returns gear numbers 1-4, have to zero it
            gear_num = char_list[0]["gear_num"] - 1
            char.gear[gear_num] = get_gear(screenshot, rects.list_rect_gearstat)
            char.uniform = get_default_uni(char.id)

            return {"result_char": char, "filepath": filepath, "gear_num":gear_num, "gear_name":gear_name}
        else:
            # return (char_list, gear_stats_list) where gear_stats_list is a list of 8 GearValue objects
            gear_result = get_gear(screenshot, rects.list_rect_gearstat)
            return {"char_list": char_list, "gear": gear_result, "filepath": filepath}
    else:
        return filepath


if __name__ == '__main__':
    time = datetime.datetime.now()

    # print(get_char_json('C:/Users/Daniel/Nox_share/Image/Screenshot_2017-03-23-22-51-31.png'))
    print(get_char_json('C:/Users/Daniel/Nox_share/Image/Screenshot_2017-03-28-12-13-38.png'))
    # print(get_char_json('C:/Users/Daniel/Nox_share/Image/Screenshot_2017-04-02-02-02-33.png'))
    print(get_char_json('C:/Users/Daniel/Nox_share/Image/Screenshot_2017-03-23-22-51-31 - Copy.jpg'))
    print(datetime.datetime.now() - time)
