# <center> 🌍 WBG Global Update Feed 🌍 </center>

[Home](index.md) | [APAC Updates](WBG_APAC.md) | [EMEA Updates](emea.md) | [Americas Updates](americas.md)

## 📅 Latest Updates

_Last updated: {{ site.time | date: "%B %d, %Y" }}_

<div class="scroll-container">
  <div class="feed-item" style="border: 1px solid #ccc; padding: 15px; margin: 20px 0; border-radius: 8px;">
<h3>
    <a href="https://www.eletimes.ai/emerging-trends-in-wide-band-gap-semiconductors-sic-and-gan-technology-for-automotive-and-energy-saving-applications</a>
    </h3>
    <p><strong>Summary:</strong> Explore how SiC and GaN technologies are transforming automotive and energy-saving applications. This article discusses the latest innovations and market trends in WBG semiconductors.</p>
  </div>
</div>

<style>
.scroll-container {
  width: 850px;          /* Adjust width */
  height: 150px;         /* Fixed height for scrolling */
  overflow: hidden;      /* Hide scrollbar for smooth effect */
  border: 1px solid #aaa;
  padding: 10px;
  position: relative;
}

.feed-item {
  position: relative;
}
</style>

<script>
const container = document.querySelector('.scroll-container');
let scrollSpeed = 0.5; // pixels per frame
let isPaused = false;

function autoScroll() {
  if (!isPaused) {
    container.scrollTop += scrollSpeed;
    if (container.scrollTop >= container.scrollHeight - container.clientHeight) {
      container.scrollTop = 0; // Reset to top
    }
  }
  requestAnimationFrame(autoScroll);
}

// Pause on hover
container.addEventListener('mouseenter', () => {
  isPaused = true;
});

container.addEventListener('mouseleave', () => {
  isPaused = false;
});

autoScroll();
</script>

## Overview
The WBG Global Update Feed is a centralized hub that aggregates information from multiple sources worldwide, ensuring stakeholders have quick access to relevant updates. The feed pulls content from:

**Official News Portals**

WBG press releases, semiconductor industry news sites, and regional business publications.

**Forums & Community Discussions**

Insights from professional forums, LinkedIn groups, and industry-specific discussion boards.

**Internal Contributions**

Curated summaries from WBG teams across different regions and business units.

This multi-source approach ensures the feed reflects real-time developments, strategic initiatives, and market trends, all in one accessible platform.
