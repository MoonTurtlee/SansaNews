<script lang="ts">
  import * as Card from "$lib/components/ui/card/index.js";
  import { type Media } from "$lib/types";
  import User from "$lib/components/User.svelte";

  let media: Media = $props();
</script>

<Card.Root class="mb-8 border-0 bg-transparent shadow-none">
  <Card.Content class="px-0 sm:px-6">
    <div
      class="bg-card border-border card-shadow flex flex-col overflow-hidden rounded-lg border-2 border-t md:h-82 md:flex-row"
    >
      <div
        class="border-border aspect-square h-full w-full shrink-0 overflow-hidden border-b-2 md:w-auto md:border-r-2 md:border-b-0"
      >
        <!-- Post image -->
        <a
          href={media.permalink}
          target="_blank"
          rel="noopener noreferrer"
          class="group relative block h-full w-full"
        >
          <img
            src={media.url}
            alt="Post de {media.username}"
            referrerpolicy="no-referrer"
            class="absolute inset-0 h-full w-full object-cover"
          />
        </a>
      </div>

      <div
        class="flex w-full min-w-0 flex-1 flex-col justify-between p-4 md:p-4"
      >
        <!-- Description -->
        <p
          class="text-foreground overflow-y-auto text-sm leading-relaxed wrap-break-word whitespace-pre-line sm:text-base"
        >
          {media.caption}
        </p>

        <!-- Footer -->
        <div
          class="border-border flex shrink-0 items-center justify-end border-t-2 pt-4"
        >
          <User
            username={media.username}
            profileLink={media.profileLink}
            profilePicture={media.profilePicture}
            datePublished={media.datePublished}
          />
        </div>
      </div>
    </div>
  </Card.Content>
</Card.Root>

<style>
  .card-shadow {
    box-shadow: 4px 4px 0px 0px var(--border);
    transition: box-shadow 300ms;
  }

  .card-shadow:hover {
    box-shadow: 6px 6px 0px 0px var(--border);
  }
</style>
