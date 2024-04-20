
    function showPhone() {
        const phoneNumber = "+1234567890";
        const phoneNumberDisplay = document.getElementById("phoneNumberDisplay");
        phoneNumberDisplay.innerHTML = "Phone number: " + phoneNumber;
    }


const nextPageUrl = 'searchResults.html';
const prevPageUrl = 'searchResults.html';

document.addEventListener('DOMContentLoaded', function () {

    const prevButton = document.querySelector('.prev');
    const nextButton = document.querySelector('.next');

    prevButton.addEventListener('click', function () {
        window.location.href = prevPageUrl;
    });

    nextButton.addEventListener('click', function () {
        window.location.href = nextPageUrl;
    });

});