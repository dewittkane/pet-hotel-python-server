import psycopg2 
import psycopg2.extras 

conn = psycopg2.connect("dbname=pet_hotel user=alexseverson", cursor_factory=psycopg2.extras.RealDictCursor)