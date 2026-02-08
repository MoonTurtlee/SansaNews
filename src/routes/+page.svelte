<script lang="ts">
  import * as Card from "$lib/components/ui/card/index.js";
  import mediaFile from "$lib/assets/media.json";
  import { Avatar } from "$lib/components/ui/avatar/index.js";

  // Time conversion
  function timeAgo(dateString: string): string {
    let date = new Date(dateString);
    let now = new Date();
    let seconds = Math.floor((now.getTime() - date.getTime()) / 1000);

    let interval = seconds / 31536000;
    if (interval > 1) return `Hace ${Math.floor(interval)} años`;

    interval = seconds / 2592000;
    if (interval > 1) return `Hace ${Math.floor(interval)} meses`;

    interval = seconds / 86400;
    if (interval > 1) return `Hace ${Math.floor(interval)} días`;

    interval = seconds / 3600;
    if (interval > 1) return `Hace ${Math.floor(interval)} horas`;

    interval = seconds / 60;
    if (interval > 1) return `Hace ${Math.floor(interval)} minutos`;

    return "Hace un momento";
  }

  // Data map
  const mediaList = mediaFile.map((media) => ({
    caption: media.caption || "Sin descripción",
    url: media.media_url,
    username: media.username,
    profileLink: "https://www.instagram.com/" + media.username,
    profilePicture: media.profile_picture_url,
    permalink: media.permalink,
    datePublished: timeAgo(media.timestamp),
  }));
</script>

<main
  class="w-full max-w-7xl mx-auto px-4 py-4 flex flex-col gap-8 min-h-screen overflow-x-hidden"
>
  <section class="w-full overflow-x-hidden">
    <!-- Card -->
    {#each mediaList as media}
      <Card.Root class="border-0 shadow-none bg-transparent mb-8">
        <Card.Content class="px-0 sm:px-6">
          <div
            class="bg-card border-2 border-border border-t card-shadow overflow-hidden flex flex-col md:flex-row md:h-82 rounded-lg"
          >
            <div
              class="w-full md:w-auto h-full aspect-square shrink-0 border-b-2 md:border-b-0 md:border-r-2 border-border overflow-hidden"
            >
              <!-- IG post image -->
              <a
                href={media.permalink}
                target="_blank"
                rel="noopener noreferrer"
                class="relative w-full h-full group block"
              >
                <img
                  src={media.url}
                  alt="Post de {media.username}"
                  referrerpolicy="no-referrer"
                  class="absolute inset-0 w-full h-full object-cover"
                />
              </a>
            </div>

            <!-- Post info -->
            <div
              class="w-full flex-1 min-w-0 p-4 md:p-4 flex flex-col justify-between"
            >
              <!-- Description -->
              <p
                class="overflow-y-auto text-sm sm:text-base text-foreground leading-relaxed whitespace-pre-line wrap-break-word"
              >
                {media.caption}
              </p>

              <!-- Footer -->
              <div
                class="pt-4 border-t-2 border-border flex items-center justify-end shrink-0"
              >
                <!-- Author info -->
                <a
                  href={media.profileLink}
                  target="_blank"
                  rel="noopener noreferrer"
                  class="flex items-center gap-2 sm:gap-3 hover:opacity-80 transition-opacity"
                >
                  <!-- Name and publish time -->
                  <div class="flex flex-col text-right min-w-0">
                    <span
                      class="text-base sm:text-base font-semibold text-foreground truncate"
                    >
                      {media.username}
                    </span>
                    <span
                      class="text-[10px] uppercase text-muted-foreground tracking-wider font-semibold whitespace-nowrap"
                    >
                      {media.datePublished}
                    </span>
                  </div>
                  <!-- Avatar -->
                  <Avatar class="h-12 w-12 sm:h-15 sm:w-15 shrink-0">
                    <img
                      src={media.profilePicture}
                      alt="Post de {media.username}"
                      referrerpolicy="no-referrer"
                      class="absolute inset-0 w-full h-full object-cover"
                    />
                  </Avatar>
                </a>
              </div>
            </div>
          </div>
        </Card.Content>
      </Card.Root>
    {/each}
  </section>
</main>

