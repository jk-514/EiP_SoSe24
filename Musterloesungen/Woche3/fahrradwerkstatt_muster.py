tasks = [[2389, 1325], [6430, 427], [10620, 1541], [10620, 4032], [12391, 1512], [19260, 14], [35100, 1282], [35504, 518], [40860, 1526], [49692, 1613], [52380, 1469], [53820, 1426], [76860, 1411], [78300, 1613], [85500, 499], [85634, 1541], [95580, 1310], [99953, 5069], [108540, 1224], [123012, 1483], [133020, 3686], [135900, 1282], [135900, 4301], [142122, 1584], [145980, 422], [173532, 408], [176220, 528], [180540, 514], [181980, 475], [184860, 1310], [184860, 5702], [189180, 1584], [189180, 3456], [194940, 499], [195270, 1656], [196380, 14], [196380, 1627], [202140, 6394], [207900, 518], [207968, 446], [209340, 1397], [210847, 470], [212220, 1512], [216540, 1656], [216540, 1541], [217980, 422], [225454, 1541], [228060, 1541], [230940, 1296], [235260, 4339], [249660, 17], [253980, 3840], [262620, 1238], [270273, 5126], [277020, 413], [277438, 494], [278460, 1627], [288540, 13], [297180, 3648], [305820, 1354], [307260, 523], [310140, 1627], [311899, 1498], [313020, 538], [315900, 504], [327420, 1382], [334620, 1469], [339398, 1584], [345123, 538], [347580, 494], [347580, 504], [363420, 1382], [372488, 3955], [373606, 13], [375140, 1526], [379633, 494], [387900, 1498], [392220, 1541], [395100, 509], [397980, 494], [399420, 1526], [408060, 3341], [411143, 1253], [416995, 16], [421446, 422], [422460, 1382], [431100, 1541], [432540, 3494], [435420, 1253], [451260, 1584], [451260, 1483], [451493, 490], [452700, 523], [459900, 1613], [461340, 514], [467100, 533], [468540, 1642], [469980, 4109], [471493, 5702], [474322, 466], [483410, 1411], [484380, 538], [484380, 1656], [488700, 509], [488700, 6106], [491580, 1541], [498780, 475], [499142, 1584], [500220, 1440], [500630, 1310], [507773, 437], [509178, 1498], [510300, 1267], [525009, 1339]]

# a) 
w = []
v = []
last_t = 0
for t, d in tasks:
    if len(w) == 0:
        w.append(d)
        v.append(0)
        continue
    last_end = last_t + w[-1]
    w.append(d + max(last_end - t,0))
    v.append(max(last_end - t,0))
    last_t = t
    
print(f'Längste Wartezeit: {max(w)}, längste Verspätung: {max(v)}')
print(f'Durchschnittliche Wartezeit: {sum(w)/len(w)}, durchschnittliche Verspätung: {sum(v)/len(v)}')

# b)
dur_day = 24*60
time_off = 16*60
time_start = 9*60
time_end = 17*60
w = [0]
v = [0]
last_t = 0
for t, d in tasks:
    last_end = last_t + w[-1]

    cur_w = 0
    start_t = t
    if last_end > t:
        start_t = last_end
        cur_w += last_end - t

    # check if start_t is in the night
    daytime = start_t % dur_day
    # if it is, we add the difference to the wait time
    if daytime < time_start or daytime > time_end:
        # late
        if daytime > time_end:
            cur_w += dur_day - daytime + time_start
        # early
        else:
            cur_w += time_start - daytime
    
    tmp_d = d
    # how many working days will he work on this task?
    days = tmp_d // (dur_day - time_off)
    cur_w += days * dur_day
    tmp_d -= days * (dur_day - time_off)
        
    cur_w += tmp_d
    
    # still needs to be during the day
    daytime_end = (t + cur_w) % dur_day
    if daytime_end < time_start or daytime_end > time_end:
        # late
        if daytime > time_end:
            cur_w += dur_day - daytime_end + time_start
        # early
        else:
            cur_w += time_start - daytime_end
    
    cur_v = max(cur_w - d,0)
    
    w.append(cur_w)
    v.append(cur_v)
    last_t = t

print()
print()
print(f'Längste Wartezeit: {max(w[1:])}, längste Verspätung: {max(v[1:])}')
print(f'Durchschnittliche Wartezeit: {sum(w[1:])/len(w[1:])}, durchschnittliche Verspätung: {sum(v[1:])/len(v[1:])}')
