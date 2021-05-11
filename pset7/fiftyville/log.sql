-- Keep a log of any SQL queries you execute as you solve the mystery.

-- 1. Take information from crime scene reports
SELECT description FROM crime_scene_reports WHERE year = 2020 AND month = 7 AND day = 28 AND street = "Chamberlin Street";
-- Theft of the CS50 duck took place at 10:15am at the Chamberlin Street courthouse. Interviews were conducted today with three witnesses who were present at the time — each of their interview transcripts mentions the courthouse.

-- 1) theft took place at 10:15am at the Chamberlin Street courthouse

-- 2. Check witness' interviews
SELECT name, transcript FROM interviews WHERE year = 2020 AND month = 7 AND day = 28 AND transcript LIKE "%thief%" ORDER BY name;
-- Eugene | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at the courthouse, I was walking by the ATM on Fifer Street and saw the thief there withdrawing some money.
-- Raymond | As the thief was leaving the courthouse, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket.
-- Ruth | Sometime within ten minutes of the theft, I saw the thief get into a car in the courthouse parking lot and drive away. If you have security footage from the courthouse parking lot, you might want to look for cars that left the parking lot in that time frame.

-- 1) thief withdrew money from the atm on Fifer Street before Eugene's arrival to the courthouse
-- 2) thief took the first flight out of town the day after theft, accomplice bought the ticket, they made a phone call for less than a minute
-- 3) around 10 minutes of the theft, the thief took the car in the courthouse parking lot

-- 3. Check Eugene's testimony : check Eugene's time of courthouse arrival, and check the atm transaction on Fifer street before that time
SELECT license_plate FROM people WHERE name = "Eugene"; -- 47592FJ
SELECT year, month, day, hour, minute, activity FROM courthouse_security_logs WHERE license_plate = "47592FJ";
-- 2020 | 7 | 26 | 13 | 22 | entrance
-- 2020 | 7 | 26 | 17 | 27 | exit
-- 2020 | 7 | 30 | 8 | 53 | entrance
-- 2020 | 7 | 30 | 15 | 45 | exit

-- Eugene did not use his car to go to the courthouse on the theft day, thus left no record of his arrival time

-- Check for the atm transactions - 1st suspect list
SELECT DISTINCT(name) FROM people
JOIN bank_accounts ON people.id = bank_accounts.person_id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE atm_transactions.account_number IN
(SELECT account_number FROM atm_transactions WHERE year = 2020 AND month = 7 AND day = 28 AND atm_location = "Fifer Street" AND transaction_type = "withdraw")
ORDER BY name;
-- Bobby
-- Danielle
-- Elizabeth
-- Ernest
-- Madison
-- Roy
-- Russell
-- Victoria


-- 4. Check Raymond's testimony : check the first flight out of town on 2020/7/29
SELECT full_name, city, hour, minute FROM flights
JOIN airports ON origin_airport_id = airports.id
WHERE year = 2020 AND month = 7 AND day = 29 ORDER BY hour;

SELECT full_name, city, hour, minute FROM flights
JOIN airports ON destination_airport_id = airports.id
WHERE year = 2020 AND month = 7 AND day = 29 ORDER BY hour;

-- thief took the flight to Heathrow Airport, London at 8:20am

-- get names of the passenger = 2nd suspect list
SELECT name FROM people WHERE passport_number IN (SELECT passport_number FROM passengers
JOIN flights ON passengers.flight_id = flights.id
WHERE year = 2020 AND month = 7 AND day = 29 AND hour = 8 AND minute = 20 AND flight_id =
(SELECT id FROM flights WHERE year = 2020 AND month = 7 AND day = 29 AND hour = 8 AND minute = 20)) ORDER BY name;
-- Bobby
-- Danielle
-- Doris
-- Edward
-- Ernest
-- Evelyn
-- Madison
-- Roger


-- 5. Check Ruth's testimony : check courthouse security logs - 3rd suspect list
SELECT name FROM people WHERE license_plate IN (SELECT license_plate FROM courthouse_security_logs
WHERE year = 2020 AND month = 7 AND day = 28 AND hour = 10 AND minute > 15 AND minute < 25 AND activity = "exit") ORDER BY name;
-- Amber
-- Danielle
-- Elizabeth
-- Ernest
-- Evelyn
-- Patrick
-- Roger
-- Russell

-- 6. Intersect three suspect list
SELECT DISTINCT(name) FROM people
JOIN bank_accounts ON people.id = bank_accounts.person_id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE atm_transactions.account_number IN
(SELECT account_number FROM atm_transactions WHERE year = 2020 AND month = 7 AND day = 28 AND atm_location = "Fifer Street" AND transaction_type = "withdraw")
INTERSECT
SELECT name FROM people WHERE passport_number IN (SELECT passport_number FROM passengers
JOIN flights ON passengers.flight_id = flights.id
WHERE year = 2020 AND month = 7 AND day = 29 AND hour = 8 AND minute = 20 AND flight_id =
(SELECT id FROM flights WHERE year = 2020 AND month = 7 AND day = 29 AND hour = 8 AND minute = 20))
INTERSECT
SELECT name FROM people WHERE license_plate IN (SELECT license_plate FROM courthouse_security_logs
WHERE year = 2020 AND month = 7 AND day = 28 AND hour = 10 AND minute > 15 AND minute < 25 AND activity = "exit") ORDER BY name;
-- Danielle
-- Ernest

-- 7. Check Raymond's testimony 2 : lookup for thief and accomplice's phone call record
SELECT name FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE year = 2020 AND month = 7 AND day = 28 AND duration < 60) ORDER BY name;
-- Bobby
-- Ernest
-- Evelyn
-- Kimberly
-- Madison
-- Roger
-- Russell
-- Victoria

SELECT name FROM people WHERE phone_number IN (SELECT receiver FROM phone_calls WHERE year = 2020 AND month = 7 AND day = 28 AND duration < 60) ORDER BY name;
-- Anna
-- Berthold
-- Doris
-- Jack
-- Jacqueline
-- James
-- Larry
-- Melissa
-- Philip

-- Final suspect : Ernest, accomplice : Berthold