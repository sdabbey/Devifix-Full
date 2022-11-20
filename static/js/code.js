const buttons = document.querySelector('.verification-modal section.content ul.buttons');
const numberField = document.querySelector(".verification-modal section.content input[type='number']");
const fields = document.querySelectorAll('.verification-modal section.content ul.buttons li button');
const sendCode = document.querySelector('section.right-content form li button.send-code');
const verificationModal = document.querySelector('.verification-modal');

setInterval(getNum, 100);
buttons.addEventListener('click', test);
sendCode.addEventListener('click', showModal);

for (n=0; n < 4; n++){
    fields[n].addEventListener('click', test);
}

function getNum(){
    const nums = numberField.value;
    for(n=0; n < 4; n++){
        if(nums[n] >= 0){
            fields[n].innerHTML = nums[n];
        }
        else{
            fields[n].innerHTML = ''
        }
    }
}

function showModal(e){
    e.preventDefault();
    verificationModal.style.display = 'grid';
}

function test(e){
    e.preventDefault();
    numberField.focus();
}





