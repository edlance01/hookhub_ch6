document.addEventListener("DOMContentLoaded", () => {
  const filterButtons = document.querySelectorAll(".filter-pill");
  const cards = document.querySelectorAll(".card");
  const emptyState = document.querySelector(".empty-state");

  cards.forEach((card, index) => {
    const accent = card.dataset.accent || "#5b4fe0";

    card.style.transition = "transform 0.18s ease, box-shadow 0.18s ease, opacity 0.4s ease";
    card.style.opacity = "0";
    card.style.transform = "translateY(8px)";
    window.setTimeout(() => {
      card.style.opacity = "1";
      card.style.transform = "translateY(0)";
    }, index * 40);

    card.addEventListener("mouseenter", () => {
      card.style.transform = "translateY(-4px)";
      card.style.boxShadow = `0 12px 24px -12px ${accent}99`;
    });
    card.addEventListener("mouseleave", () => {
      card.style.transform = "translateY(0)";
      card.style.boxShadow = "none";
    });
  });

  filterButtons.forEach((button) => {
    button.addEventListener("click", () => {
      filterButtons.forEach((b) => b.classList.remove("is-active"));
      button.classList.add("is-active");

      const filter = button.dataset.filter;
      let visibleCount = 0;

      cards.forEach((card) => {
        const matches = filter === "All" || card.dataset.eventType === filter;
        card.classList.toggle("hidden", !matches);
        if (matches) visibleCount += 1;
      });

      emptyState.classList.toggle("hidden", visibleCount !== 0);
    });
  });
});
