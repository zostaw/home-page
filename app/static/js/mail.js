
const links = document.querySelectorAll("[data-part1][data-part2][data-part3][data-part4]");
for (const link of links) {
  const attrs = link.dataset;
  link.setAttribute(
    "href",
    `mailto:${attrs.part1}${attrs.part3}@${attrs.part4}.${attrs.part2}?subject=${attrs.subject}`
  );
  link.textContent = `${attrs.part1}${attrs.part3}@${attrs.part4}.${attrs.part2}`;
}
