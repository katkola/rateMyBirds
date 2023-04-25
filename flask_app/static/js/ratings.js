function yup(buttonValue) {
    document.forms[0].rating_value.value = buttonValue;
    var elements = document.getElementsByClassName('btn-star')
    for (let i = 0; i < elements.length; i++) {
        elements[i].style.backgroundColor = 'rgb(251, 244, 205)';
    }
    for (let i = 1; i <= buttonValue; i++) {
        document.getElementById('btn' + i).style.backgroundColor = "gold";
    }
}