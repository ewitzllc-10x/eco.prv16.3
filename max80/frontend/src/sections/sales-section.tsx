import CardLink from "../components/card-link";
import { CardLink_cids } from "../_cids";
import { CardLink_styles } from "../_styles";
import { cardLinkData as cardLinkDataContent } from "../content";
/** Sales section. */
export default function SalesSection({ cardLinkData = cardLinkDataContent } = {}) {
  return (
    <div className="flex flex-col gap-4" data-cid="n53">
      <div className="flex flex-col gap-1" data-cid="n54">
        <h2 className="block text-color-001 text-xl font-semibold leading-7" data-cid="n55" data-component="heading">
          Sales
        </h2>
      </div>
      <div className="grid gap-4 grid-rows-3 grid-cols-3 max-md:grid-rows-7 max-md:grid-cols-1 md:max-lg:grid-rows-4 md:max-lg:grid-cols-2" data-cid="n56">
        {cardLinkData.map((d, i) => <CardLink key={i} d={d} cids={CardLink_cids[i]} styles={CardLink_styles[i]} />)}
      </div>
    </div>
  );
}
