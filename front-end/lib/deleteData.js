export default async function deleteData(url, id) {
  console.log("running deleteData");
  try {
    let response = await fetch(`${url}${id}`, {
      method: "DELETE",
    });
    if (response.status === 204) {
      return "Delete successful.";
    } else {
      throw new Error("Something went wrong");
    }
  } catch (err) {
    console.log(err);
  }
}
