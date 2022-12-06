export default async function postData(url, data) {
  try {
    console.log("running postData");
    let response = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
    if (response.status === 201) {
      return response.json();
    } else {
      throw new Error("Something went wrong");
    }
  } catch (err) {
    console.log(err);
  }
}
