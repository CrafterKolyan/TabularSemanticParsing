from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, SelectField
from wtforms.validators import DataRequired


class SQLForm(FlaskForm):
    database = SelectField("Database",
                           choices=['cre_Doc_Template_Mgt', 'scholar', 'school_finance', 'club_1', 'music_4',
                                    'customers_and_addresses', 'music_2', 'program_share', 'race_track', 'museum_visit',
                                    'store_1', 'chinook_1', 'cinema', 'university_basketball', 'tvshow',
                                    'school_player', 'sakila_1', 'world_1', 'journal_committee', 'flight_company',
                                    'local_govt_mdm', 'school_bus', 'twitter_1', 'movie_1', 'local_govt_in_alabama',
                                    'college_1', 'game_1', 'sports_competition', 'election', 'document_management',
                                    'voter_2', 'climbing', 'train_station', 'protein_institute', 'wedding',
                                    'company_employee', 'performance_attendance', 'tracking_orders', 'perpetrator',
                                    'yelp', 'academic', 'insurance_policies', 'small_bank_1', 'browser_web',
                                    'customers_and_invoices', 'singer', 'city_record', 'film_rank', 'phone_1',
                                    'poker_player', 'machine_repair', 'battle_death', 'loan_1', 'insurance_fnol',
                                    'department_store', 'phone_market', 'scientist_1', 'icfp_1', 'company_office',
                                    'decoration_competition', 'solvency_ii', 'orchestra', 'concert_singer', 'ship_1',
                                    'entrepreneur', 'behavior_monitoring', 'product_catalog',
                                    'student_transcripts_tracking', 'roller_coaster', 'soccer_2', 'course_teach',
                                    'activity_1', 'tracking_software_problems', 'allergy_1', 'store_product',
                                    'culture_company', 'soccer_1', 'manufacturer', 'wrestler', 'college_2',
                                    'election_representative', 'coffee_shop', 'student_assessment',
                                    'cre_Doc_Tracking_DB', 'employee_hire_evaluation', 'network_1', 'apartment_rentals',
                                    'hr_1', 'architecture', 'products_gen_characteristics', 'bike_1', 'wine_1',
                                    'musical', 'voter_1', 'college_3', 'baseball_1', 'epinions_1',
                                    'customers_campaigns_ecommerce', 'mountain_photos', 'device', 'music_1', 'csu_1',
                                    'body_builder', 'aircraft', 'dorm_1', 'real_estate_properties', 'railway',
                                    'flight_2', 'company_1', 'county_public_safety', 'book_2', 'customer_deliveries',
                                    'tracking_share_transactions', 'hospital_1', 'local_govt_and_lot', 'ship_mission',
                                    'department_management', 'network_2', 'party_people', 'cre_Theme_park', 'farm',
                                    'imdb', 'cre_Doc_Control_Systems', 'inn_1', 'customer_complaints', 'pilot_record',
                                    'station_weather', 'swimming', 'riding_club', 'assets_maintenance',
                                    'tracking_grants_for_research', 'restaurant_1', 'candidate_poll', 'news_report',
                                    'e_learning', 'car_1', 'medicine_enzyme_interaction', 'pets_1', 'products_for_hire',
                                    'flight_1', 'debate', 'e_government', 'entertainment_awards', 'wta_1',
                                    'driving_school', 'game_injury', 'geo', 'theme_gallery',
                                    'cre_Drama_Workshop_Groups', 'manufactory_1', 'dog_kennels', 'restaurants',
                                    'shop_membership', 'customers_card_transactions', 'customers_and_products_contacts',
                                    'student_1', 'match_season', 'flight_4', 'gas_company', 'party_host',
                                    'cre_Docs_and_Epenses', 'gymnast', 'workshop_paper', 'formula_1', 'storm_record',
                                    'insurance_and_eClaims'])
    query = StringField('Natural Language Query', validators=[DataRequired()])
    submit = SubmitField('Evaluate')
