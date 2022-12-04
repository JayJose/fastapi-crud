export default function formatDate(date) {
  let options = { hour: "2-digit", minute: "2-digit" };
  let newDate = new Date(date);
  return newDate.toLocaleDateString("en-US", options);
}
