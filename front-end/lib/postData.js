export default async function postData(url, data) {
  try {
    let response = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
    if (response.status === 201) {
      console.log("POST successful!");
      return response.json();
    }
  } catch (err) {
    console.log(err);
  }
}
