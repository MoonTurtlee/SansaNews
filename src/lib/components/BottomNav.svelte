<script lang="ts">
    import { page } from '$app/state';
    
    let { navItems } = $props();
    let navItemsFiltered = $derived(navItems.filter((item: any) => item.label !== "Sobre Nosotros"));
</script>

<div>
    <!-- Bottom Navigation -->
    <nav class="fixed bottom-0 left-0 right-0 bg-background border-t border-muted z-50 md:hidden">
        <ul class="flex justify-around">
            {#each navItemsFiltered as item}
                {@const isActive = page.url.pathname === item.href}
                <li>
                    <a 
                        href={item.href} 
                        class="flex flex-col items-center py-2 text-sm transition-colors"
                        class:text-primary={isActive}
                        class:text-muted-foreground={!isActive}
                    >     
                        <item.icon class="h-5 w-5 mb-1" />
                        {item.shortLabel}
                    </a>
                </li>
            {/each}
        </ul>
    </nav>
</div>