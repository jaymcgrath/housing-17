'''
    Template for the State of Housing Neighboorhood Profile Data Sheet

    A word smith might want to improve the names of the fields (just saying...)
'''

nbhood_template = [\
[ 0,0 ,'neighboorhood'],\
[ 4,2 ,'pop_2000'],\
[ 4,3 ,'pop_2014'],\
[ 4,4 ,'med_income_2000'],\
[ 4,5 ,'med_income_2014'],\
[ 4,6 ,'poverty_rate_2000'],\
[ 4,7 ,'poverty_rate_2014'],\
[ 4,9 ,'housetotal_2000'],\
[ 4,10 ,'housetotal_2014'],
[ 5,2 ,'pop_white_2000'],\
[ 5,3 ,'pop_white_2014'],\
[ 5,4 ,'white_med_income_2000'],\
[ 5,5 ,'white_med_income_2014'],\
[ 5,6 ,'white_poverty_rate_2000'],\
[ 5,7 ,'white_poverty_rate_2014'],\
[ 5,9 ,'single_person_house_2000'],\
[ 5,10 ,'single_person_house_2014'],\
[ 6,2 ,'black_pop_2000'],\
[ 6,3 ,'black_pop_2014'],\
[ 6,4 ,'black_med_income_2000'],\
[ 6,5 ,'black_med_income_2014'],\
[ 6,6 ,'black_poverty_rate_2000'],\
[ 6,7 ,'black_poverty_rate_2014'],\
[ 6,9 ,'house_w_children_2000'],\
[ 6,10 ,'house_w_children_2014'],\
[ 7,2 ,'asian_pop_2000'],\
[ 7,3 ,'asian_pop_2014'],\
[ 7,4 ,'asian_med_income_2000'],\
[ 7,5 ,'asian_med_income_2014'],\
[ 7,6 ,'asian_poverty_rate_2000'],\
[ 7,7 ,'asian_poverty_rate_2014'],\
[ 7,9 ,'foreign_born_2000'],\
[ 7,10 ,'foreign_born_2014'],\
[ 8,2 ,'hispanic_pop_2000'],\
[ 8,3 ,'hispanic_pop_2014'],\
[ 8,4 ,'hispanic_med_income_2000'],\
[ 8,5 ,'hispanic_med_income_2014'],\
[ 8,6 ,'hispanic_poverty_rate_2000'],\
[ 8,7 ,'hispanic_poverty_rate_2014'],\
[ 8,9 ,'exp_disabilities_2000'],\
[ 8,10 ,'exp_disabilities_2014'],\
[ 9,2 ,'hawaiian_pop_2000'],\
[ 9,3 ,'hawaiian_pop_2014'],\
[ 9,4 ,'hawaiian_med_income_2000'],\
[ 9,5 ,'hawaiian_med_income_2014'],\
[ 9,6 ,'hawaiian_poverty_rate_2000'],\
[ 9,7 ,'hawaiian_poverty_rate_2014'],\
[ 9,9 ,'over65_2000'],\
[ 9,10 ,'over65_2014'],\
[ 10,2 ,'native_amer_pop_2000'],\
[ 10,3 ,'native_amer_pop_2014'],\
[ 10,4 ,'native_amer_med_income_2000'],\
[ 10,5 ,'native_amer_med_income_2014'],\
[ 10,6 ,'native_amer_poverty_rate_2010'],\
[ 10,7 ,'native_amer_poverty_rate_2014'],\
[ 14,2 ,'housing_units_total_2000'],\
[ 14,3 ,'housing_units_total_2010'],\
[ 14,4 ,'housing_units_total_2011'],\
[ 14,5 ,'housing_units_total_2012'],\
[ 14,6 ,'housing_units_total_2013'],\
[ 14,7 ,'housing_units_total_2014'],\
[ 14,8 ,'housing_units_total_2015'],\
[ 15,2 ,'housing_single_fam_2000'],\
[ 15,3 ,'housing_single_fam_2010'],\
[ 15,4 ,'housing_single_fam_2011'],\
[ 15,5 ,'housing_single_fam_2012'],\
[ 15,6 ,'housing_single_fam_2013'],\
[ 15,7 ,'housing_single_fam_2014'],\
[ 15,8 ,'housing_single_fam_2015'],\
[ 16,2 ,'housing_mult_fam_2000'],\
[ 16,3 ,'housing_mult_fam_2010'],\
[ 16,4 ,'housing_mult_fam_2011'],\
[ 16,5 ,'housing_mult_fam_2012'],\
[ 16,6 ,'housing_mult_fam_2013'],\
[ 16,7 ,'housing_mult_fam_2014'],\
[ 16,8 ,'housing_mult_fam_2015'],\
[ 17,2 ,'regulate_aford_units_2000'],\
[ 17,3 ,'regulate_aford_units_2010'],\
[ 17,4 ,'regulate_aford_units_2011'],\
[ 17,5 ,'regulate_aford_units_2012'],\
[ 17,6 ,'regulate_aford_units_2013'],\
[ 17,7 ,'regulate_aford_units_2014'],\
[ 17,8 ,'regulate_aford_units_2015'],\
[ 18,2 ,'city_fun_aford_2000'],\
[ 18,3 ,'city_fun_aford_2010'],\
[ 18,4 ,'city_fun_aford_2011'],\
[ 18,5 ,'city_fun_aford_2012'],\
[ 18,6 ,'city_fun_aford_2013'],\
[ 18,7 ,'city_fun_aford_2014'],\
[ 18,8 ,'city_fun_aford_2015'],\
[ 19,2 ,'new_res_total_permits_2000'],\
[ 19,3 ,'new_res_total_permits_2010'],\
[ 19,4 ,'new_res_total_permits_2011'],\
[ 19,5 ,'new_res_total_permits_2012'],\
[ 19,6 ,'new_res_total_permits_2013'],\
[ 19,7 ,'new_res_total_permits_2014'],\
[ 19,8 ,'new_res_total_permits_2015'],\
[ 20,2 ,'new_res_sing_fam_permits_2000'],\
[ 20,3 ,'new_res_sing_fam_permits_2010'],\
[ 20,4 ,'new_res_sing_fam_permits_2011'],\
[ 20,5 ,'new_res_sing_fam_permits_2012'],\
[ 20,6 ,'new_res_sing_fam_permits_2013'],\
[ 20,7 ,'new_res_sing_fam_permits_2014'],\
[ 20,8 ,'new_res_sing_fam_permits_2015'],\
[ 21,2 ,'new_res_mult_fam_permits_2000'],\
[ 21,3 ,'new_res_mult_fam_permits_2010'],\
[ 21,4 ,'new_res_mult_fam_permits_2011'],\
[ 21,5 ,'new_res_mult_fam_permits_2012'],\
[ 21,6 ,'new_res_mult_fam_permits_2013'],\
[ 21,7 ,'new_res_mult_fam_permits_2014'],\
[ 21,8 ,'new_res_mult_fam_permits_2015'],\
[ 25,1 ,'mult_fam_rental_total'],\
[ 25,2 ,'mult_fam_rental_studio'],\
[ 25,3 ,'mult_fam_rental_1br'],\
[ 25,4 ,'mult_fam_rental_2br'],\
[ 25,5 ,'mult_fam_rental_3br'],\
[ 25,6 ,'mult_fam_rental_owner'],\
[ 25,9 ,'owner_total_2000'],\
[ 25,10 ,'owner_total_2014'],\
[ 26,1 ,'ave_rent_overall'],\
[ 26,2 ,'ave_rent_studio'],\
[ 26,3 ,'ave_rent_1br'],\
[ 26,4 ,'ave_rent_2br'],\
[ 26,5 ,'ave_rent_3br'],\
[ 26,6 ,'ave_rent_owner'],\
[ 26,9 ,'owner_white_2000'],\
[ 26,10 ,'owner_white_2014'],\
[ 27,1 ,'rent_vacancy_rate_total'],\
[ 27,2 ,'rent_vacancy_rate_studio'],\
[ 27,3 ,'rent_vacancy_rate_1br'],\
[ 27,4 ,'rent_vacancy_rate_2br'],\
[ 27,5 ,'rent_vacancy_rate_3br'],\
[ 27,6 ,'rent_vacancy_rate_owner'],\
[ 27,9 ,'owner_black_2000'],\
[ 27,10 ,'owner_black_2014'],\
[ 28,9 ,'owner_asian_2000'],\
[ 28,10 ,'owner_asian_2014'],\
[ 29,9 ,'owner_latin_2000'],\
[ 29,10 ,'owner_latin_2014'],\
[ 30,2 ,'ave_portland_studio_aford'],\
[ 30,3 ,'ave_portland_1br_aford'],\
[ 30,4 ,'ave_portland_2br_aford'],\
[ 30,5 ,'ave_portland_3br_aford'],\
[ 30,6 ,'ave_portland_owner_aford'],\
[ 30,9 ,'owner_hawaiian_2000'],\
[ 30,10 ,'owner_hawaiian_2014'],\
[ 31,0 , '3-Person Extremely Low-Income'],\
[ 31,2 , '3people_extr_low_income_studio_aford'],\
[ 31,3 , '3people_extr_low_income_1br_aford'],\
[ 31,4 , '3people_extr_low_income_2br_aford'],\
[ 31,5 , '3people_extr_low_income_3br_aford'],\
[ 31,6 , '3people_extr_low_income_owner_aford'],\
[ 31,9 ,'owner_native_am_2000'],\
[ 31,10 , 'owner_native_am_2010'],\
[ 32,2 , '3people_low_income_studio_aford'],\
[ 32,3 , '3people_low_income_1br_aford'],\
[ 32,4 , '3people_low_income_2br_aford'],\
[ 32,5 , '3people_low_income_3br_aford'],\
[ 32,6 , '3people_low_income_owner_aford'],\
[ 33,2 , '3people_mod_income_studio_aford'],\
[ 33,3 , '3people_low_income_1br_aford'],\
[ 33,4 , '3people_low_income_2br_aford'],\
[ 33,5 , '3people_low_income_3br_aford'],\
[ 33,6 , '3people_low_income_owner_aford'],\
[ 34,2 , 'couple_family_studio_aford'],\
[ 34,3 , 'couple_family_1br_aford'],\
[ 34,4 , 'couple_family_2br_aford'],\
[ 34,5 , 'couple_family_3br_aford'],\
[ 34,6 , 'couple_family_owner_aford'],\
[ 35,2 , 'white_studio_aford'],\
[ 35,3 , 'white_1br_aford'],\
[ 35,4 , 'white_2br_aford'],\
[ 35,5 , 'white_3br_aford'],\
[ 35,6 , 'white_owner_aford'],\
[ 35,9 ,'med_home_price_2000'],\
[ 36,2 , 'black_studio_aford'],\
[ 36,3 , 'black_1br_afordv'],\
[ 36,4 , 'black_2br_aford'],\
[ 36,5 , 'black_3br_aford'],\
[ 36,6 , 'black_owner_aford'],\
[ 36,9 ,'med_home_price_2010'],\
[ 37,2 , 'latino_studio_aford'],\
[ 37,3 , 'latino_1br_aford'],\
[ 37,4 , 'latino_2br_aford'],\
[ 37,5 , 'latino_3br_aford'],\
[ 37,6 , 'latino_owner_aford'],\
[ 37,9 , 'med_home_price_2011'],\
[ 38,2 , 'native_studio_aford'],\
[ 38,3 , 'native_1br_aford'],\
[ 38,4 , 'native_2br_aford'],\
[ 38,5 , 'native_3br_aford'],\
[ 38,6 , 'native_owner_aford'],\
[ 38,9 ,'med_home_price_2012'],\
[ 39,2 , 'asian_studio_aford'],\
[ 39,3 , 'asian_1br_aford'],\
[ 39,4 , 'asian_2br_aford'],\
[ 39,5 , 'asian_3br_aford'],\
[ 39,6 , 'asian_owner_aford'],\
[ 39,9 ,'med_home_price_2013'],\
[ 40,2 , 'senior_studio_aford'],\
[ 40,3 , 'senior_1br_aford'],\
[ 40,4 , 'senior_2br_aford'],\
[ 40,5 , 'senior_3br_aford'],\
[ 40,6 , 'senior_owner_aford'],\
[ 40,9 ,'med_home_price_2014'],\
[ 41,2 , 'single_mom_studio_aford'],\
[ 41,3 , 'single_mom_1br_aford'],\
[ 41,4 , 'single_mom_2br_aford'],\
[ 41,5 , 'single_mom_3br_aford'],\
[ 41,6 , 'single_mom_owner_aford'],\
[ 41,9 ,'med_home_price_2015'],\
[ 42,2 , 'foreign_studio_aford'],\
[ 42,3 , 'foreign_1br_aford'],\
[ 42,4 , 'foreign_2br_aford'],\
[ 42,5 , 'foreign_3br_aford'],\
[ 42,6 , 'foreign_owner_aford'],
[ -1, -1, 'ThatsAllFolks']]

def getNeighboorhoodField(idx):
    l = nbhood_template[idx]
    row = l[0]
    col = l[1]
    field = l[2]
    idx = idx + 1
    return row, col, field, idx
