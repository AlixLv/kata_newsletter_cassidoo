//  Given a year, return the day of the week for New Year's Day of that year.

const weekDays = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    0: "Sunday",
};


function newYearsDay(year){
    let searchDate = new Date(`${year}-01-01`);
    let searchDay = searchDate.getDay()

    let days = Object.keys(weekDays);
    let newDay;

    days.forEach((day) => {
        if(searchDay == day){
            newDay = weekDays[day]
        } 
    });
    return newDay
};
        
let day = newYearsDay(2024);
console.log(day)
