import React from 'react';
import algoliasearch from 'algoliasearch/lite';
import {
  Configure,
  Hits,
  InstantSearch,
  Pagination,
  SearchBox,
  Highlight,
  Snippet,
  Stats,
  RefinementList
} from 'react-instantsearch';

import { Panel } from './Panel';

import type { Hit } from 'instantsearch.js';

import './App.css';

import TypesenseInstantSearchAdapter from "typesense-instantsearch-adapter";

const typesenseInstantsearchAdapter = new TypesenseInstantSearchAdapter({
  server: {
    apiKey: "xyz",
    nodes: [
      {
        // host: "localhost",
        host: "https://2095-138-51-33-148.ngrok-free.app",
        // host: "mighty-bugs-train.loca.lt",
        // port: 8108,
        protocol: "https"
      }
    ]
  },
  // The following parameters are directly passed to Typesense's search API endpoint.
  //  So you can pass any parameters supported by the search endpoint below.
  //  queryBy is required.
  additionalSearchParameters: {
    query_by: "comment_body",
    filter_by: "has_img_url:true",
    limit_hits: 1000
    // limit_hits: 4
    // include_fields: ["board_description"]
  }
});
const searchClient = typesenseInstantsearchAdapter.searchClient;

const future = { preserveSharedStateOnUnmount: true };

export function App() {
  return (
    <div>
      <header className="header">
        <h1 className="header-title">
          <a href="/">Galaxy Zoo Talk Search</a>
        </h1>
        <p className="header-subtitle">
          created at{' '}
          <a href="https:www.dotastronomy.com">
            .Astronomy 13
          </a>
        </p>
      </header>

      <div className="container">
        <InstantSearch
          searchClient={searchClient}
          indexName="comments"
          future={future}
        >
          <Configure hitsPerPage={10} />
          <div className="search-panel" id="foo">
            <div className="filter-pane">
              <h2 className="filter-header">Board Filter</h2>
              <div className="search-panel__filters"></div>
              <RefinementList attribute="board_title" />
            </div>


            <div className="search-panel__results">
              <SearchBox placeholder="" className="searchbox" />

              <Hits hitComponent={Hit} />

              <div className="pagination">
                <Pagination />
              </div>
              <Stats />
            </div>
          </div>
        </InstantSearch>
      </div>
    </div>
  );
}

type HitProps = {
  hit: Hit;
};



function Hit({ hit }: HitProps) {
  // console.log(hit.img_url)
  const comment_url = "https://www.zooniverse.org/projects/zookeeper/galaxy-zoo/talk/1269/" + hit.discussion_id + "?comment=" + hit.comment_id
  // https://www.zooniverse.org/projects/zookeeper/galaxy-zoo/talk/1269/656301?comment=4809026
  return (
    <article>
      <div>
        <i>
          <Highlight attribute="board_title" hit={hit} />
        </i>
        <br></br>
        {/* src={hit.img_url} */}
        {/* 'https://panoptes-uploads.zooniverse.org/subject_location/33147e8e-2b0e-4bb7-9c67-e1932c34c78e.jpeg' */}
        <img crossOrigin="anonymous" src={hit.img_url} style={{ width: '125px', height: '125px'}} />
      </div>
      <h3>
        <Snippet attribute="discussion_title" hit={hit}></Snippet>, User <Snippet attribute="comment_user_id" hit={hit}></Snippet>
      </h3>
      {/* <h3>
        
      </h3> */}
      <p>
        <Snippet hit={hit} attribute="comment_body" />
      </p>
      <a href={comment_url}>Link</a>
    </article>
  );
}
