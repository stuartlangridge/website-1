---
date: "2025-05-31T12:00:00+01:00"
title: "An Amazing Start"
slug: "an-amazing-start"
author: "Alan Pope"
---

# What a week!

First, **thank you** to everyone who has [added](https://add.nerdydaytrips.org/) new venues, filed [bugs](https://github.com/NerdyDayTrips/website/issues), reviewed & edited locations, and provided feedback and support. Thank you _so_ much. I had no idea whether people would actually want to contribute to something like this. I'm *delighted* you all have.

We have had contributions from around the globe, including from the USA, UK, Japan, Croatia, Germany, Canada, and no doubt more I missed.

We've also had conversations with other people who were also enthusiastic to revive this type of resource. I had no idea other people were so passionate about this too! That's so validating to hear.

We've made a bunch of changes over the last week, mostly around the look of the site, the logo, and the process for adding new venues. There's more to do there, though. If you know a nearby friendly web developer with CSS smarts, I'd appreciate their input/help to make a good looking, robust and responsive website.

The site was *somewhat* thrown together (as you can probably tell), so I'm sure there are bugs on mobile devices and desktop browsers.

## Adding sites with copy & paste

I wanted to make adding new venues straightforward, but not too easy that we get flooded with spam submissions. It's important to me (and I'm sure to you too) that non-nerds and nerds alike are able to share their favourite or recently discovered locations as easily as possible.

So, with that in mind, today, I added the ability on the [add a venue](https://add.nerdydaytrips.org/) page to just paste an [Open Street Map](https://openstreetmap.org/) (OSM) URL in, and have our site pick out the lat/long and other details, directly from OSM.

[{{< image
src="/images/2025/05/add-with-osm-url-thumb.png"
alt="The new submission option" >}}](/images/2025/05/add-with-osm-url.png)

It does require an OSM [way](https://wiki.openstreetmap.org/wiki/Way) style URL, which often isn't just the link your browser shows. However, they're easy to discover on the OSM site. 

> When on OSM, click the little arrow-with-question-mark icon in the toolbar, then point at the venue you wish to add. On the left will be a pop-out panel with "Nearby features", and "Enclosing features". Pick the most appropriate "way", and your URL will update. That's the one to paste into [add a venue](https://add.nerdydaytrips.org/) page.

If there are problems with this new feature, do let us know with an [issue](https://github.com/NerdyDayTrips/website/issues) report, or jump on our [Discord](https://discord.gg/VJKJ5EzgXA) server to chat directly with us.

## Managing duplicates

One other thing I haven't quite figured out yet, but plan to, is dealing with duplicate submissions. For example, we had three submissions for [Bletchley Park](https://nerdydaytrips.org/daytrip/eu/gb/bletchley-park/) in one day.

Ideally the page where you add new venues should have the smarts to do that duplicate search for you and respond with "We already have venue x (with a link)", with options to edit it in GitHub, or add the new site anyway, in case the search is wrong, or the new addition compliments or supplements the existing ones nearby.

## Rejection feedback

I am also aware that the site doesn't provide any feedback to submitters whose venues were not accepted. This is unfortunately a by-product of not really wanting to know and store all your personal details, such as an email address, to tell you about the rejection. I don't want to have the burden of carrying everyone's personal data, and emailing people.

I'll start a topic over on [GitHub Discussions](https://github.com/NerdyDayTrips/website/discussions) if anyone has any bright ideas!

## Thanks again

Once more, massive thanks to everyone who has helped this week.

If you'd like to discuss anything in this blog, join our [Discord](https://discord.gg/VJKJ5EzgXA) or start a topic in our [GitHub Discussions](https://github.com/NerdyDayTrips/website/discussions)

Oh, and keep on [adding venues](https://add.nerdydaytrips.org/)!
