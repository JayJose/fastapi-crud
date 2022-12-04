export default async function getData(url, setData) {
  try {
    let req = await fetch(url, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });
    let res = await req.json();
    if (req.status === 200) {
      setData(res);
    }
  } catch (err) {
    console.log(err);
  }
}
