var hour = document.getElementById("hour");
var minute = document.getElementById("minute");
var second = document.getElementById("second");
var ampm = document.getElementById("ampm");

function getTime() {
  let newHour = new Date().getHours();
  let newMinute = new Date().getMinutes();
  let newSecond = new Date().getSeconds();
  let newAmpm = "AM";

  if (newHour > 12) {
    newHour = newHour - 12;
    ampm = "PM";
  } else if (newHour === 12) {
    newHour = newHour + 12;
    ampm = "AM";
  }

  if (newHour < 10) {
    newHour = "0" + newHour;
  } else {
    newHour = newHour;
  }

  if (newMinute < 10) {
    newMinute = "0" + newMinute;
  } else {
    newMinute = newMinute;
  }

  if (newSecond < 10) {
    newSecond = "0" + newSecond;
  } else {
    newSecond = newSecond;
  }

  hour.innerText = newHour;
  minute.innerText = newMinute;
  second.innerText = newSecond;
  ampm.innerText = newAmpm;

  setInterval(getTime, 1000);
}
getTime();
