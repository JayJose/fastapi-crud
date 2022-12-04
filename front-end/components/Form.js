import { useRef, useState } from "react";

export default function Form() {
  const [message, setMessage] = useState();

  const usernameRef = useRef();
  const passwordRef = useRef();

  async function onSubmit(e) {
    e.preventDefault();
    try {
      let req = await fetch("http://localhost:8000/api/users/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: usernameRef.current.value,
          password: passwordRef.current.value,
        }),
      });
      let res = await req.json();
      if (req.status === 201) {
        console.log(res);
        setMessage("User created successfully!");
        console.log(message);
      } else {
        setMessage("Something went wrong.");
        console.log(message);
      }
    } catch (err) {
      console.log(err);
    }
  }

  //     try {
  //       let res = await fetch("https://httpbin.org/post", {
  //         method: "POST",
  //         body: JSON.stringify({
  //           name: name,
  //           password: password,
  //         }),
  //       });
  //       let resJson = await res.json();
  //       if (res.status === 200) {
  //         setName("");
  //         setEmail("");
  //         setMessage("User created successfully");
  //       } else {
  //         setMessage("Some error occured");
  //       }
  //     } catch (err) {
  //       console.log(err);
  //     }
  //   };

  return (
    <div className="App">
      <form onSubmit={onSubmit}>
        <label htmlFor="username">Username</label>
        <input ref={usernameRef} type="text" id="username" />
        <label htmlFor="password">Password</label>
        <input ref={passwordRef} type="password" id="password" />
        <button type="submit">Submit</button>

        {/* <div className="message">{message ? <p>{message}</p> : null}</div> */}
      </form>
    </div>
  );
}
