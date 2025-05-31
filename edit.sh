#!/bin/bash

set -e

# Usage:
#   cd content/daytrip
#   echo eu/gb/dale-abbey.md >menu.txt
#   # Fill menu.txt with filenames
#   ../../edit.sh

function next_file() {
    filename=$(head -n1 menu.txt)
    echo ${filename} >>done.txt
    mv menu.txt menu.txt~
    tail -n+2 menu.txt~ >menu.txt
    echo ${filename}
}

function last_file() {
    # Back up two files, because we've consumed the current one already
    mv menu.txt menu.txt~
    tail -n2 done.txt >menu.txt
    cat menu.txt~ >>menu.txt
    mv done.txt done.txt~
    head -n-2 done.txt~ >done.txt
}

function get_tag() {
    tag="$1"
    file="$2"
    grep "^${tag}:" "${file}" | sed -e "s,^${tag}: \\?,," -e "s/['\"]//g"
}

function parse_lat() {
    latlon="$1"
    echo ${latlon} \
        | sed -e "s/^[^0-9.-]*\\([0-9.-]\\+\\),.*/\\1/"
}

function parse_lng() {
    latlon="$1"
    echo ${latlon} \
        | sed -e "s/^[^0-9.-]*[0-9.-]\\+,\\([0-9.-]\\+\\).*/\\1/"
}

while :; do
    file=$(next_file)

    slug=$(get_tag slug ${file})
    sensible-browser "https://nerdydaytrips.org/${slug}/"

    lat=$(get_tag lat ${file})
    lng=$(get_tag lng ${file})
    sensible-browser "https://www.openstreetmap.org/?mlat=${lat}&mlon=${lng}#map=17/${lat}/${lng}"

    search=$(get_tag title ${file} | sed -e "s/ /+/g")
    sensible-browser "https://duckduckgo.com/?q=${search}&t=vivaldi&ia=web"

    while :; do
        echo ${file}
        cat ${file}
        echo "[p]rint [u]rl [r]evert [g]eolocation [s]lug/file"
        echo -n "[e]dit [n]ext [P]revious [D]elete [q]uit > "
        read -n1 action
        echo
        case $action in
            p)
                echo ${file}
                cat ${file}
                ;;
            u)
                read -p "URL: " url
                if grep -q "^external_url:" ${file}; then
                    sed -i -e "s,external_url:.*\$,external_url: ${url}," ${file}
                else
                    sed -i -e "/^title:/iexternal_url: ${url}" ${file}
                fi
                ;;
            r)
                git co -- ${file}
                ;;
            g)
                read -p "lat,long: " latlong
                lat=$(parse_lat ${latlong})
                lng=$(parse_lng ${latlong})
                sed -i \
                    -e "s/^lat:.*\$/lat: ${lat}/" \
                    -e "s/^lng:.*\$/lng: ${lng}/" \
                    ${file}
                ;;
            n)
                break
                ;;
            s)
                read -p "slug: " slug
                sed -i -e "s,^slug:.*\$,slug: ${slug}," ${file}
                mv ${file} ${slug#daytrip/}.md
                file=${slug#daytrip/}.md
                ;;
            e)
                sensible-editor ${file}
                ;;
            P)
                last_file
                break
                ;;
            D)
                rm ${file}
                break
                ;;
            q)
                exit 0
                ;;
        esac
    done
done
