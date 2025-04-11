function generatePassword() {
    const letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const numbers = "0123456789";
    const symbols = "!@#$%^&*()-_=+[]{}";

    let password = "";

    for (let i = 0; i < 6; i++) {
        password += letters.charAt(Math.floor(Math.random() * letters.length));
    }
    for (let i = 0; i < 2; i++) {
        password += numbers.charAt(Math.floor(Math.random() * numbers.length));
    }
    password += symbols.charAt(Math.floor(Math.random() * symbols.length));

    // Shuffle
    password = password.split('').sort(() => 0.5 - Math.random()).join('');

    document.getElementById("passwordBox").value = password;
}

function copyPassword() {
    const copyText = document.getElementById("passwordBox");
    copyText.select();
    copyText.setSelectionRange(0, 99999);
    document.execCommand("copy");
    alert("Password copied to clipboard!");
}
