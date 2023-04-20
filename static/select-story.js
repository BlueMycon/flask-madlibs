
document.getElementById("select-story").addEventListener("change", handleStorySelect)

async function handleStorySelect(evt) {
  evt.preventDefault();
  const story = evt.target.value;
  const questionsHTML = await getQuestionsHTML(story);
  document.getElementById("questions-container").innerHTML = questionsHTML;
}

async function getQuestionsHTML(storyName) {
  const response = await axios.get(
   "/questions",
    {params: {story_name: storyName }}
  );
  return response.data;
}