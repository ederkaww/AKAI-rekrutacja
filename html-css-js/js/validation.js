const form = document.getElementById('form');
const firstName = document.getElementById('first-name');
const lastName = document.getElementById('last-name');
const email = document.getElementById('email');
const frontendCheckbox = document.getElementById('frontend-checkbox');
const backendCheckbox = document.getElementById('backend-checkbox');
const mobileCheckbox = document.getElementById('mobile-checkbox');
const graphicsCheckbox = document.getElementById('graphics-checkbox');


form.addEventListener('submit', e => {
    e.preventDefault();

    validateInputs();
});

const setError = (element, message) => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = message;
    inputControl.classList.add('error');
}

const setSuccess = element => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = '';
    inputControl.classList.add('success');
    inputControl.classList.remove('error');
};

const isValidEmail = email => {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}


const validateInputs = () => {
    const firstNameValue = firstName.value.trim();
    const lastNameValue = lastName.value.trim();
    const emailValue = email.value.trim();

    console.log(frontendCheckbox.checked)
    if(firstNameValue === '') {
        setError(firstName, 'Imię jest wymagane');
    } else {
        setSuccess(firstName);
    }

    if(lastNameValue === '') {
        setError(lastName, 'Nazwisko jest wymagane');
    } else {
        setSuccess(lastName);
    }

    if(emailValue === '') {
        setError(email, 'Email jest wymagany');
    } else if (!isValidEmail(emailValue)) {
        setError(email, 'Wprowadź prawidłowy email');
    } else {
        setSuccess(email);
    }

    if(!frontendCheckbox.checked && !backendCheckbox.checked && !mobileCheckbox.checked && !graphicsCheckbox.checked){
        document.getElementById('our-sections').style.color = "#ff3860";
    } else {
        document.getElementById('our-sections').style.color = "white";
    }
}
