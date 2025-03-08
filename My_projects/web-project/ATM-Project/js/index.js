var info = [
    {
        id: 100,
        fullName: "Khuda Dad Shafaee",
        pin: 112233,
        password: "king@123",
        balance: 100000
    }
]

let cover = document.getElementById("cover")
login = `
    <div class="login">
        <h1>Login Page</h1>
        <p>
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Optio deserunt architecto excepturi commodi eligendi minus, dolorum accusantium autem ipsam repellat quae ea quaerat sit, odio aperiam dolorem culpa deleniti incidunt.
        </p>
        <img src="./images/lock.png" width= "140px">
        <input type="number" placeholder="Enter your PIN: ">
        <input type="password" placeholder="Enter your password">
        <input type="submit" value="Login">
    </div>
`
cover.innerHTML = login;
