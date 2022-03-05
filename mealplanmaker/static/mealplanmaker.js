document.addEventListener('DOMContentLoaded', function() {
});

function calculateCalories() {

  setTimeout(function () {

    // Get form
    var form = document.forms["tdeeform"];

    // Get gender value
    var gender = form.elements["gender"];
    if(gender[0].checked) {
      gender_value = 5;
    }
    else {
      gender_value = -161;
    }
    console.log(gender_value);

    // Activity level array
    var activity_multiplier = new Array();
    activity_multiplier[1] = 1.2;
    activity_multiplier[2] = 1.375;
    activity_multiplier[3] = 1.55;
    activity_multiplier[4] = 1.725;
    activity_multiplier[5] = 1.9;

    // Get activity level value
    activitylevel_value = 0;
    var activityselected = form.elements["activitylevel"].value;
    activitylevel_value = activity_multiplier[activityselected];
    console.log(activitylevel_value);

    // Get weight
    var weight = form.elements["weight"].value;
    console.log(weight);

    // Get height
    var height = form.elements["height"].value;
    console.log(height);

    // Get age
    var age = form.elements["age"].value;
    console.log(age);

    // Calculate calories
    calories_result = ((weight * 10) + (height * 6.25) - (5 * age) + gender_value) * activitylevel_value;

    // Update view
    document.getElementById('calories_result').innerHTML = calories_result.toFixed(0);


  }, 1);

}

