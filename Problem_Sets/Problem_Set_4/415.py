import datetime, math

def is_leap(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def parse_date(date):
    date_info, tz = date.split()
    dt = datetime.datetime.strptime(date_info, "%Y-%m-%d")
    short_dt = datetime.datetime(year = 2026, month = dt.month, day = dt.day)
    sign = 1 if tz[3] == "+" else -1
    hour_offset = int(tz[4:6])
    min_offset = int(tz[7:])
    dt_utc = short_dt - datetime.timedelta(hours = hour_offset, minutes = min_offset) * sign
    return dt_utc

a = input()
b = input()
d1 = parse_date(a)
d2 = parse_date(b)
diff = (d1 - d2).total_seconds() / 86400
if diff < 0:
    print(math.ceil(diff) + 365)
else:
    print(math.ceil(diff))



















# def print_all_info(date: datetime) -> list:
#     return [date.day, date.month, date.year]

# # def parse_date(date1, date2):
# #     # parsing date 1
# #     date1_info, tz1_info = date1.split()
# #     if not is_leap(int(date2[0:4])) and date1[5:7] == "02" and date1[8:10] == "29":
# #         date1[8:10] = "28"
# #     parsed_d1 = datetime.datetime.strptime(date1_info, "%Y-%m-%d")

# #     # parsing date 2
# #     date2_info, tz2_info = date2.split()
# #     parsed_d2 = datetime.datetime.strptime(date2_info, "%Y-%m-%d")

# #     # temporary check WILL BE DELETED
# #     # print(print_all_info(parsed_d1), print_all_info(parsed_d2), sep = "\n")

# #     # converting to utc
# #     sign1 = 1 if tz1_info[3] == "+" else -1
# #     sign2 = 1 if tz2_info[3] == "+" else -1
# #     hours1_offset = int(tz1_info[4:6])
# #     hours2_offset = int(tz2_info[4:6])
# #     minutes1_offset = int(tz1_info[7:])
# #     minutes2_offset = int(tz2_info[7:])
# #     dt1_utc = parsed_d1
# #     dt2_utc = parsed_d2
# #     final_dt1 = datetime.datetime(year = 2026, month = dt1_utc.month, day = dt1_utc.day)
# #     final_dt2 = datetime.datetime(year = 2026, month = dt2_utc.month, day = dt2_utc.day)
# #     date_diff = int((final_dt1 - final_dt2).total_seconds() / 86400)
# #     print(f"Date 1 in UTC: {dt1_utc} \n Date 2 in UTC: {dt2_utc}")
# #     print(date_diff if date_diff >= 0 else date_diff + 365)

# def parse_date(date1, date2):
#     # parsing date 1
#     date1_info, tz1_info = date1.split()
#     if not is_leap(int(date2[0:4])) and date1[5:7] == "02" and date1[8:10] == "29":
#         date1[8:10] = "28"
#     parsed_d1 = datetime.datetime.strptime(date1_info, "%Y-%m-%d")

#     # parsing date 2
#     date2_info, tz2_info = date2.split()
#     parsed_d2 = datetime.datetime.strptime(date2_info, "%Y-%m-%d")

#     # temporary check WILL BE DELETED
#     print(print_all_info(parsed_d1), print_all_info(parsed_d2), sep = "\n")

#     # converting to utc
#     sign1 = 1 if tz1_info[3] == "+" else -1
#     sign2 = 1 if tz2_info[3] == "+" else -1
#     hours1_offset = int(tz1_info[4:6])
#     hours2_offset = int(tz2_info[4:6])
#     minutes1_offset = int(tz1_info[7:])
#     minutes2_offset = int(tz2_info[7:])
#     dt1_utc = parsed_d1 - datetime.timedelta(hours = hours1_offset, minutes = minutes1_offset) * sign1
#     dt2_utc = parsed_d2 - datetime.timedelta(hours = hours2_offset, minutes = minutes2_offset) * sign2
#     final_dt1 = datetime.datetime(year = 2026, month = dt1_utc.month, day = dt1_utc.day)
#     final_dt2 = datetime.datetime(year = 2026, month = dt2_utc.month, day = dt2_utc.day)
#     date_diff = int((final_dt1 - final_dt2).total_seconds() / 86400)
#     print(f"Date 1 in UTC: {dt1_utc}\nDate 2 in UTC: {dt2_utc}")
#     print(math.ceil(date_diff if date_diff >= 0 else date_diff + 365))


# a = input()
# b = input()

# parse_date(a, b)