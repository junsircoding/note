var emailRegex = /^((?!(白|班)).)*$/gm;

function isValidEmail(input){
    return emailRegex.test(input);
}