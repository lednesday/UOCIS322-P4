"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
from sys import setdlopenflags
import arrow
from arrow import Arrow
from typing import List, Dict, Tuple


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#

TOP_SPEEDS: dict = {'to200': 34, 'to400': 32, 'to600': 30, 'to1000': 28}


def open_time(control_dist_km: float, brevet_dist_km: float, brevet_start_time: Arrow):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600,
          or 1000 (the only official ACP brevet distances)
       brevet_start_time:  A date object (arrow)
    Returns:
       A date object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    # note: times are rounded to the nearest minute
    # special case: if control_dist_km == 0, open_time is brevet_start_time
    if control_dist_km == 0:
        open_time = brevet_start_time
    # for distances below 200 - normal case
    elif control_dist_km <= 200:
        (hours, minutes) = h_m_at_speed(control_dist_km, TOP_SPEEDS['to200'])
        open_time = brevet_start_time.shift(
            hours=hours, minutes=round(minutes))
    # special case: if brevet_dist == 200, controle distances can be up to 20% longer
    # but the controle times remain fixed at their 200 values
    elif (brevet_dist_km == 200) and (control_dist_km <= round(200 + 200 * .2)):
        open_time = brevet_start_time.shift(
            hours=5, minutes=53)
    # for distances below 400
    elif control_dist_km <= 400:
        first_200: Tuple[int, float] = h_m_at_speed(200, TOP_SPEEDS['to200'])
        remaining_distance = control_dist_km - 200
        second_200: Tuple[int, float] = h_m_at_speed(
            remaining_distance, TOP_SPEEDS['to400'])
        (total_hours, total_minutes) = (
            first_200[0] + second_200[0]), (first_200[1] + second_200[1])
        # summing minutes may result in more than 60, so we need to carry over into hour
        if total_minutes >= 60:
            (total_hours, total_minutes) = carry_m_to_h(
                total_hours, total_minutes)
        open_time = brevet_start_time.shift(
            hours=total_hours, minutes=round(total_minutes))
    # special case: if brevet_dist == 400km, controle distances can be up to 20% longer
    # but the controle times remain fixed at their 400km values
    elif (brevet_dist_km == 400) and (control_dist_km <= round(400 + 400 * .2)):
        open_time = brevet_start_time.shift(
            hours=12, minutes=8)
    # for distances below 600
    elif control_dist_km <= 600:
        first_200: Tuple[int, float] = h_m_at_speed(200, TOP_SPEEDS['to200'])
        second_200: Tuple[int, float] = h_m_at_speed(
            200, TOP_SPEEDS['to400'])
        remaining_distance = control_dist_km - 400
        third_200: Tuple[int, float] = h_m_at_speed(
            remaining_distance, TOP_SPEEDS['to600'])
        (total_hours, total_minutes) = (
            first_200[0] + second_200[0]) + third_200[0], (first_200[1] + second_200[1] + third_200[1])
        # summing minutes may result in more than 60, so we need to carry over into hour
        if total_minutes >= 60:
            (total_hours, total_minutes) = carry_m_to_h(
                total_hours, total_minutes)
        open_time = brevet_start_time.shift(
            hours=total_hours, minutes=round(total_minutes))
    # special case: if brevet_dist == 600, controle distances can be up to 20% longer
    # but the controle times remain fixed at their 600km values
    elif (brevet_dist_km == 600) and (control_dist_km <= round(600 + 600 * .2)):
        open_time = brevet_start_time.shift(
            hours=18, minutes=48)
    # a 1000km brevet may have a final controle up to 20% greater than 1000
    elif control_dist_km < round(1000 + 1000 * .2):
        if control_dist_km > 1000:
            control_dist_km = 1000
        first_200: Tuple[int, float] = h_m_at_speed(200, TOP_SPEEDS['to200'])
        second_200: Tuple[int, float] = h_m_at_speed(
            200, TOP_SPEEDS['to400'])
        third_200: Tuple[int, float] = h_m_at_speed(
            200, TOP_SPEEDS['to600'])
        remaining_distance = control_dist_km - 600
        final_400: Tuple[int, float] = h_m_at_speed(
            remaining_distance, TOP_SPEEDS['to1000'])
        (total_hours, total_minutes) = (
            first_200[0] + second_200[0]) + third_200[0] + final_400[0], (first_200[1] + second_200[1] + third_200[1] + final_400[1])
        # summing minutes may result in more than 60, so we need to carry over into hour
        if total_minutes >= 60:
            (total_hours, total_minutes) = carry_m_to_h(
                total_hours, total_minutes)
        open_time = brevet_start_time.shift(
            hours=total_hours, minutes=round(total_minutes))

    # should never end up here
    else:
        # indicate error for now by returning datetime arrow with all 0's
        open_time = arrow.get(
            '0000-00-00 00:00:00', 'YYYY-MM-DD HH:mm:ss')
    return open_time
    #  return arrow.now()


def h_m_at_speed(dist: float, speed: int) -> Tuple[int, float]:
    # keeping minutes as a float because if I round here and then sum later
    # there will be inappropriate rounding errors
    hours = int(dist // speed)
    minutes = dist % speed / speed * 60
    return (hours, minutes)


def carry_m_to_h(hours: int, minutes: float) -> Tuple[int, float]:
    hours += int(minutes // 60)
    minutes = minutes % 60
    return(hours, minutes)


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  A date object (arrow)
    Returns:
       A date object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """

    # special case: if control_dist_km == 0, return brevet_start_time + 1 hour
    if control_dist_km == 0:
        return brevet_start_time.shift(hours=1)

    return arrow.now()


def main():
    start_time = arrow.get('2021-02-20 14:00:00', 'YYYY-MM-DD HH:mm:ss')
    print("test open_time 100 (s.b. 16:56): ", open_time(100, 200, start_time))
    print("test open_time 890 (s.b. 19:09): ",
          open_time(890, 1000, start_time))
    print("test open_time 299 (s.b. 22:59)", open_time(299, 1000, start_time))
    print("test open_time 300 (s.b. 23:00)", open_time(300, 1000, start_time))
    print("test open_time 301 (s.b. 23:02)", open_time(301, 1000, start_time))
    print("test open_time 1000 (s.b. 23:05)",
          open_time(1000, 1000, start_time))
    print("test open_time 1000 (s.b. 23:05)",
          open_time(1005, 1000, start_time))


if __name__ == "__main__":
    main()
