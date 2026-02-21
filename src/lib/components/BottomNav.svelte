<script lang="ts">
  import { page } from "$app/state";
  import type { BottomNavItem, NavGroup } from "./SuperNav.svelte";

  let {
    bottomNavItems,
    activeGroup,
    bottomHidden,
  }: {
    bottomNavItems: BottomNavItem[];
    activeGroup: NavGroup | null;
    bottomHidden: boolean;
  } = $props();

  // An item is active if:
  // 1. his route is the current route or
  // 2. his `group` is the active group
  function isActive(item: BottomNavItem): boolean {
    if (page.url.pathname === item.href) return true;
    if (activeGroup && item.group === activeGroup) return true;
    return false;
  }
</script>

<nav
  class="fixed bottom-0 left-0 right-0 bg-background border-t-2 z-50 lg:hidden transition-transform duration-300"
  class:translate-y-full={bottomHidden}
>
  <ul class="flex justify-around">
    {#each bottomNavItems as item}
      <li>
        <a
          href={item.href}
          class="flex flex-col items-center py-2 text-sm transition-colors"
          class:text-primary={isActive(item)}
          class:text-muted-foreground={!isActive(item)}
        >
          <item.icon class="h-4 w-4 mb-1" />
          {item.label}
        </a>
      </li>
    {/each}
  </ul>
</nav>